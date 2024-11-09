import fs from "node:fs"
import yaml from "yaml"
import converter from "swagger2openapi"

const options = {
	patch: true,
	warnOnly: true,
	resolve: true,
	preprocess: (swagger) => {
		// Function to recursively process schema objects
		function fixSchemaTypes(obj, path = "") {
			if (typeof obj !== "object" || obj === null) return

			// Check for schema object with type property
			if (obj.schema && obj.schema.type === "int") {
				console.log(`Found 'int' type at ${path}.schema.type`)
				obj.schema.type = "integer"
			}

			// Check direct type property
			if (obj.type === "int") {
				console.log(`Found 'int' type at ${path}.type`)
				obj.type = "integer"
			}

			// Process all nested objects
			for (const [key, value] of Object.entries(obj)) {
				if (typeof value === "object" && value !== null) {
					const newPath = path ? `${path}.${key}` : key
					// Handle arrays
					if (Array.isArray(value)) {
						for (const [index, item] of value.entries()) {
							fixSchemaTypes(item, `${newPath}[${index}]`)
						}
					} else {
						fixSchemaTypes(value, newPath)
					}
				}
			}
		}

		// Process the entire swagger object
		fixSchemaTypes(swagger, "root")

		// Additional safety check for YAML string values
		function deepStringReplace(obj) {
			if (typeof obj !== "object" || obj === null) return

			for (const [key, value] of Object.entries(obj)) {
				if (typeof value === "string") {
					if (value.trim() === "int") {
						console.log(`Found string 'int' value at property ${key}`)
						obj[key] = "integer"
					}
				} else if (typeof value === "object") {
					deepStringReplace(value)
				}
			}
		}

		deepStringReplace(swagger)

		// Log the processed swagger object for debugging
		fs.writeFileSync("processed-swagger.json", JSON.stringify(swagger, null, 2))
		return swagger
	},
}

// Read the input file
const processSwagger = async () => {
	try {
		const data = await fs.promises.readFile("oandav20.json", "utf8")
		const swagger = JSON.parse(data)

		// Convert to OpenAPI 3.0
		converter.convertObj(swagger, options, (err, options) => {
			if (err) {
				console.error("Error converting:", err)
				return
			}

			// Additional post-processing to catch any remaining 'int' types
			function postProcessTypes(obj) {
				if (typeof obj !== "object" || obj === null) return

				if (obj.type === "int") {
					console.log("Found int type during post-processing")
					obj.type = "integer"
				}

				for (const value of Object.values(obj)) {
					if (typeof value === "object") {
						postProcessTypes(value)
					}
				}
			}

			postProcessTypes(options.openapi)

			// Convert to YAML and write to file
			const output = yaml.stringify(options.openapi)

			// Final safety check on the YAML string
			const finalOutput = output.replace(/type: int\b/g, "type: integer")
			fs.writeFileSync("openapi.yaml", finalOutput, "utf8")
			console.log("Conversion completed successfully!")

			// Verify the output
			const resultContent = fs.readFileSync("openapi.yaml", "utf8")
			if (resultContent.includes("type: int")) {
				console.error(
					'Warning: Output still contains "type: int". Please check processed-swagger.json for debugging.'
				)

				// Find and log occurrences
				const lines = resultContent.split("\n")
				for (const [index, line] of lines.entries()) {
					if (line.includes("type: int")) {
						console.log(`Found "type: int" at line ${index + 1}: ${line}`)
					}
				}
			}
		})
	} catch (err) {
		console.error("Error reading or parsing input file:", err)
	}
}

processSwagger()
