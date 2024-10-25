import prisma from "../utils/prisma.js";
import { spawn } from "child_process";

export const createModel = async (req, res) => {
	const { title, link, src, img } = req.body;
	try {
		const model = await prisma.model.create({
			data: {
				title,
				uniqueLink: link,
				src,
				img,
			},
		});
		return res.status(200).json({ message: "Successfully Added The Model", model });
	} catch (error) {
		return res.status(500).json({ message: "Failed To Add The Model", error: error.message });
	}
};

export const readModels = async (req, res) => {
	try {
		const models = await prisma.model.findMany();

		return res.status(200).json({ message: "Successfully Retrieved All Models", count: models.length, models });
	} catch (error) {
		return res.status(500).json({ message: "Failed To Retrieve The Models", error: error.message });
	}
};

export const deleteModel = async (req, res) => {
	const { id } = req.params;
	try {
		const deleteModel = await prisma.model.delete({
			where: {
				id,
			},
		});

		return res.status(200).json({ message: "Successfully Deleted The Model", deleteModel });
	} catch (error) {
		return res.status(500).json({ message: "Failed To Delete The Model", error: error.message });
	}
};

export const searchModels = async (req, res) => {
	const { prompt } = req.params;
	console.log("Search models", prompt);
	try {
		const models = await prisma.model.findMany({
			where: {
				title: {
					contains: prompt,
					mode: "insensitive",
				},
			},
		});

		return res.status(200).json({ message: "Successfully Searched The Models DB", no_results: models.length, models });
	} catch (error) {
		return res.status(500).json({ message: "Failed To Search The Models DB", error: error.message });
	}
};
