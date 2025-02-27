import { createCanvas } from "canvas";
import * as fs from "fs";

const canvas = createCanvas(200, 200);
const ctx = canvas.getContext("2d");
ctx.fillStyle = "red";
ctx.fillRect(0, 0, 100, 100);
const buffer = canvas.toBuffer("image/png");
fs.writeFileSync("test.png", buffer);
