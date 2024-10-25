import { Router } from "express";
const rootRouter = Router();

import modelsRouter from "./models.js";

rootRouter.use("/models", modelsRouter);

export default rootRouter;
