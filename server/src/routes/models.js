import { Router } from "express";

import { createModel, deleteModel, readModels, searchModels } from "../controllers/models.js";
import { scrapeModels } from "../middlewares/models.js";
const modelRouter = Router();

modelRouter.post("/", createModel);

modelRouter.get("/", readModels);

modelRouter.delete("/:id", deleteModel);

modelRouter.get("/:prompt", scrapeModels, searchModels);

export default modelRouter;
