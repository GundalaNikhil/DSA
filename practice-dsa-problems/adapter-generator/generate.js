const fs = require("fs");

if (process.argv.length < 4) {
  process.exit(1);
}

const metadataPath = process.argv[2];
const lang = process.argv[3];

const content = fs.readFileSync(metadataPath, "utf8");
const meta = JSON.parse(content);

// --------------------
// Struct preprocessing
// --------------------
const structs = {};
if (meta.structs) {
  if (Array.isArray(meta.structs)) {
    meta.structs.forEach((s) => (structs[s.name] = s));
  } else {
    Object.assign(structs, meta.structs);
  }
}

function getBaseType(type) {
  if (type.endsWith("[]")) return type.slice(0, -2);
  return type;
}

function isStructArrayType(type) {
  return type.endsWith("[]") && !!structs[type.slice(0, -2)];
}

// --------------------
// JAVA GENERATOR
// --------------------
function generateJava(meta) {
  const lines = [];
  lines.push(`class Adapter {`);
  lines.push(`    static Object run(JSONArray args) {`);

  const callArgs = [];

  meta.parameters.forEach((p, i) => {
    const type = p.type;
    const name = p.name;

    if (type === "int") {
      lines.push(`        int ${name} = args.getInt(${i});`);
      callArgs.push(name);
    } else if (type === "long") {
      lines.push(`        long ${name} = args.getLong(${i});`);
      callArgs.push(name);
    } else if (type === "string" || type === "String") {
      lines.push(`        String ${name} = args.getString(${i});`);
      callArgs.push(name);
    } else if (type === "int[]") {
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        int[] ${name} = new int[arr${i}.length()];`);
      lines.push(`        for (int j = 0; j < arr${i}.length(); j++) {`);
      lines.push(`            ${name}[j] = arr${i}.getInt(j);`);
      lines.push(`        }`);
      callArgs.push(name);
    } else if (type === "long[]") {
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        long[] ${name} = new long[arr${i}.length()];`);
      lines.push(`        for (int j = 0; j < arr${i}.length(); j++) {`);
      lines.push(`            ${name}[j] = arr${i}.getLong(j);`);
      lines.push(`        }`);
      callArgs.push(name);
    } else if (type === "string[]" || type === "String[]") {
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        String[] ${name} = new String[arr${i}.length()];`);
      lines.push(`        for (int j = 0; j < arr${i}.length(); j++) {`);
      lines.push(`            ${name}[j] = arr${i}.getString(j);`);
      lines.push(`        }`);
      callArgs.push(name);
    } else if (type === "int[][]") {
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        int[][] ${name} = new int[arr${i}.length()][];`);
      lines.push(`        for (int r = 0; r < arr${i}.length(); r++) {`);
      lines.push(`            JSONArray row = arr${i}.getJSONArray(r);`);
      lines.push(`            ${name}[r] = new int[row.length()];`);
      lines.push(`            for (int c = 0; c < row.length(); c++) {`);
      lines.push(`                ${name}[r][c] = row.getInt(c);`);
      lines.push(`            }`);
      lines.push(`        }`);
      callArgs.push(name);
    } else if (type === "long[][]") {
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        long[][] ${name} = new long[arr${i}.length()][];`);
      lines.push(`        for (int r = 0; r < arr${i}.length(); r++) {`);
      lines.push(`            JSONArray row = arr${i}.getJSONArray(r);`);
      lines.push(`            ${name}[r] = new long[row.length()];`);
      lines.push(`            for (int c = 0; c < row.length(); c++) {`);
      lines.push(`                ${name}[r][c] = row.getLong(c);`);
      lines.push(`            }`);
      lines.push(`        }`);
      callArgs.push(name);
    } else if (isStructArrayType(type)) {
      const base = getBaseType(type);
      const def = structs[base];
      lines.push(`        JSONArray arr${i} = args.getJSONArray(${i});`);
      lines.push(`        List<Solution.${base}> ${name} = new ArrayList<>();`);
      lines.push(`        for (int k = 0; k < arr${i}.length(); k++) {`);
      lines.push(`            JSONArray row = arr${i}.getJSONArray(k);`);
      const ctorArgs = def.fields
        .map((f, idx) => {
          if (f.type === "int") return `row.getInt(${idx})`;
          if (f.type === "long") return `row.getLong(${idx})`;
          if (f.type === "string") return `row.getString(${idx})`;
          return "null";
        })
        .join(", ");
      lines.push(`            ${name}.add(new Solution.${base}(${ctorArgs}));`);
      lines.push(`        }`);
      callArgs.push(name);
    }
  });

  lines.push(`        Solution sol = new Solution();`);
  lines.push(
    `        return sol.${meta.functionName}(${callArgs.join(", ")});`
  );
  lines.push(`    }`);
  lines.push(`}`);

  return lines.join("\n");
}

// --------------------
// PYTHON GENERATOR
// --------------------
function generatePython(meta) {
  const lines = [];
  lines.push(`def adapter(args):`);

  const callArgs = [];

  meta.parameters.forEach((p, i) => {
    const type = p.type;
    const name = p.name;

    if (isStructArrayType(type)) {
      const base = getBaseType(type);
      lines.push(`    ${name} = [${base}(*x) for x in args[${i}]]`);
      callArgs.push(name);
    } else {
      callArgs.push(`args[${i}]`);
    }
  });

  lines.push(`    sol = Solution()`);
  lines.push(`    return sol.${meta.functionName}(${callArgs.join(", ")})`);

  return lines.join("\n");
}

// --------------------
// C++ GENERATOR
// --------------------
function generateCpp(meta) {
  const lines = [];
  lines.push(`json adapter(const json& args) {`);

  const callArgs = [];

  meta.parameters.forEach((p, i) => {
    const type = p.type;
    const name = p.name;

    if (type === "int") {
      lines.push(`    int ${name} = args[${i}].get<int>();`);
      callArgs.push(name);
    } else if (type === "long") {
      lines.push(`    long long ${name} = args[${i}].get<long long>();`);
      callArgs.push(name);
    } else if (type === "string") {
      lines.push(`    string ${name} = args[${i}].get<string>();`);
      callArgs.push(name);
    } else if (type === "int[]") {
      lines.push(`    vector<int> ${name} = args[${i}].get<vector<int>>();`);
      callArgs.push(name);
    } else if (type === "long[]") {
      lines.push(
        `    vector<long long> ${name} = args[${i}].get<vector<long long>>();`
      );
      callArgs.push(name);
    } else if (type === "string[]") {
      lines.push(
        `    vector<string> ${name} = args[${i}].get<vector<string>>();`
      );
      callArgs.push(name);
    } else if (type === "int[][]") {
      lines.push(
        `    vector<vector<int>> ${name} = args[${i}].get<vector<vector<int>>>();`
      );
      callArgs.push(name);
    } else if (type === "long[][]") {
      lines.push(
        `    vector<vector<long long>> ${name} = args[${i}].get<vector<vector<long long>>>();`
      );
      callArgs.push(name);
    } else if (isStructArrayType(type)) {
      const base = getBaseType(type);
      const def = structs[base];
      lines.push(`    vector<${base}> ${name};`);
      lines.push(`    for (const auto& row : args[${i}]) {`);
      const fields = def.fields.map((f, idx) => {
        if (f.type === "int") return `row[${idx}].get<int>()`;
        if (f.type === "long") return `row[${idx}].get<long long>()`;
        if (f.type === "string") return `row[${idx}].get<string>()`;
        return "";
      });
      lines.push(`        ${name}.push_back(${base}{${fields.join(", ")}});`);
      lines.push(`    }`);
      callArgs.push(name);
    }
  });

  lines.push(`    Solution sol;`);
  lines.push(
    `    auto res = sol.${meta.functionName}(${callArgs.join(", ")});`
  );
  lines.push(`    return json(res);`);
  lines.push(`}`);

  return lines.join("\n");
}

// --------------------
// JS GENERATOR
// --------------------
function generateJs(meta) {
  const lines = [];
  lines.push(`function adapter(args) {`);

  const callArgs = [];

  meta.parameters.forEach((p, i) => {
    const type = p.type;
    const name = p.name;

    if (isStructArrayType(type)) {
      const base = getBaseType(type);
      const def = structs[base];
      lines.push(`  const ${name} = args[${i}].map(row => ({`);
      def.fields.forEach((f, idx) => {
        lines.push(`    ${f.name}: row[${idx}],`);
      });
      lines.push(`  }));`);
      callArgs.push(name);
    } else {
      lines.push(`  const ${name} = args[${i}];`);
      callArgs.push(name);
    }
  });

  lines.push(`  const sol = new Solution();`);
  lines.push(`  return sol.${meta.functionName}(${callArgs.join(", ")});`);
  lines.push(`}`);

  return lines.join("\n");
}

// --------------------
// DISPATCH
// --------------------
let result = "";
if (lang === "java") result = generateJava(meta);
else if (lang === "python") result = generatePython(meta);
else if (lang === "cpp") result = generateCpp(meta);
else if (lang === "js" || lang === "javascript") result = generateJs(meta);

console.log(result);
