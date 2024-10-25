import { spawn } from "child_process";

export const scrapeModels = async (req, res, next) => {
	const { prompt } = req.params;

	const pythonProcess = spawn("python", ["../scraper/main.py", prompt]);

	let result = "";

	pythonProcess.stdout.on("data", (data) => {
		result += data.toString();
	});

	pythonProcess.stderr.on("data", (data) => {
		console.error(`stderr: ${data}`);
		res.status(500).send(`Error: ${data}`);
	});

	// pythonProcess.on("close", (code) => {
	// 	console.log(`Python script finished with code ${code}`);
	// 	    res.send(result);
	// });

	pythonProcess.on("close", (code) => {
		console.log(`Python script finished with code ${code}`);
		next();
	});
};
