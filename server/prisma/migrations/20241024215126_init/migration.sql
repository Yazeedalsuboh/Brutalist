-- CreateTable
CREATE TABLE "Model" (
    "id" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "uniqueLink" TEXT NOT NULL,
    "src" TEXT NOT NULL,
    "img" TEXT NOT NULL,
    "promptId" TEXT,

    CONSTRAINT "Model_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Prompt" (
    "id" TEXT NOT NULL,
    "input" TEXT NOT NULL,

    CONSTRAINT "Prompt_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Model_uniqueLink_key" ON "Model"("uniqueLink");

-- AddForeignKey
ALTER TABLE "Model" ADD CONSTRAINT "Model_promptId_fkey" FOREIGN KEY ("promptId") REFERENCES "Prompt"("id") ON DELETE SET NULL ON UPDATE CASCADE;
