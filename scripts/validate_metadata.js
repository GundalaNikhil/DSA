const fs = require("fs");
const path = require("path");

const PRIMITIVES = new Set([
  "int",
  "long",
  "string",
  "boolean",
  "double",
  "void",
  "char",
  "Integer",
  "Long",
  "String",
  "Boolean",
  "Double",
  "Character", // Wrappers
]);

// Helper to normalize type (handle List<T> -> T[])
function normalizeType(type) {
  let current = type;
  while (current.startsWith("List<") && current.endsWith(">")) {
    current = current.substring(5, current.length - 1) + "[]";
  }
  return current;
}

function getBaseType(type) {
  let current = normalizeType(type);
  while (current.endsWith("[]")) {
    current = current.slice(0, -2);
  }
  return current;
}

function isValidType(type, structs) {
  const base = getBaseType(type);
  if (PRIMITIVES.has(base)) return true;
  if (structs && structs[base]) return true;
  return false;
}

function validateMetadata(filePath, meta) {
  const errors = [];

  let structsMap = {};
  if (Array.isArray(meta.structs)) {
    meta.structs.forEach((s) => {
      structsMap[s.name] = s;
    });
  } else if (meta.structs) {
    structsMap = meta.structs;
  }

  // ---- Function name ----
  if (!meta.functionName || typeof meta.functionName !== "string") {
    errors.push("functionName must be a non-empty string");
  }

  // ---- Parameters ----
  if (!Array.isArray(meta.parameters)) {
    errors.push("parameters must be an array");
  } else {
    const seen = new Set();
    meta.parameters.forEach((p, i) => {
      if (!p.name || !p.type) {
        errors.push(`parameter[${i}] missing name or type`);
        return;
      }
      if (seen.has(p.name)) {
        errors.push(`duplicate parameter name: ${p.name}`);
      }
      seen.add(p.name);

      if (!isValidType(p.type, structsMap)) {
        errors.push(`invalid parameter type: ${p.type}`);
      }
    });
  }

  // ---- Return type ----
  if (!meta.returnType || !isValidType(meta.returnType, structsMap)) {
    errors.push(`invalid returnType: ${meta.returnType}`);
  }

  // ---- Structs Usage Check ----
  const usedTypes = new Set();

  if (Array.isArray(meta.parameters)) {
    meta.parameters.forEach((p) => {
      usedTypes.add(getBaseType(p.type));
    });
  }

  if (meta.returnType) {
    usedTypes.add(getBaseType(meta.returnType));
  }

  for (const name in structsMap) {
    const def = structsMap[name];
    if (!Array.isArray(def.fields) || def.fields.length === 0) {
      errors.push(`struct ${name} must have fields`);
      continue;
    }

    const fieldNames = new Set();
    for (const field of def.fields) {
      if (!field.name || !field.type) {
        errors.push(`struct ${name} has invalid field`);
        continue;
      }

      if (fieldNames.has(field.name)) {
        errors.push(`duplicate field ${field.name} in struct ${name}`);
      }
      fieldNames.add(field.name);

      if (!isValidType(field.type, structsMap)) {
        errors.push(`invalid type ${field.type} in struct ${name}`);
      }

      if (structsMap[field.type]) {
        errors.push(`nested struct not allowed: ${field.type} in ${name}`);
      }

      const fieldBase = getBaseType(field.type);
      if (structsMap[fieldBase]) {
        usedTypes.add(fieldBase);
      }
    }
  }

  // Transitive reachability
  let changed = true;
  while (changed) {
    changed = false;
    for (const name in structsMap) {
      if (usedTypes.has(name)) {
        const def = structsMap[name];
        if (def.fields) {
          def.fields.forEach((f) => {
            const fBase = getBaseType(f.type);
            if (structsMap[fBase] && !usedTypes.has(fBase)) {
              usedTypes.add(fBase);
              changed = true;
            }
          });
        }
      }
    }
  }

  for (const name in structsMap) {
    if (!usedTypes.has(name)) {
      errors.push(`struct ${name} defined but never used`);
    }
  }

  return errors;
}

function traverseAndValidate(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      traverseAndValidate(fullPath);
    } else if (entry.isFile() && entry.name.endsWith(".json")) {
      if (fullPath.includes("-metadata")) {
        try {
          const content = fs.readFileSync(fullPath, "utf8");
          const meta = JSON.parse(content);
          const validationErrors = validateMetadata(fullPath, meta);
          if (validationErrors.length > 0) {
            console.log(`\nFAIL: ${fullPath}`);
            validationErrors.forEach((e) => console.log(`  - ${e}`));
          }
        } catch (e) {
          console.log(`\nERROR parsing ${fullPath}: ${e.message}`);
        }
      }
    }
  }
}

const targetDir = path.resolve(__dirname, "../practice-dsa-problems");
console.log(`Validating metadata in: ${targetDir}`);
if (fs.existsSync(targetDir)) {
  traverseAndValidate(targetDir);
  console.log("\nValidation complete.");
} else {
  console.error("Target directory not found!");
}
