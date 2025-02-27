declare module "canvas" {
  export function createCanvas(width: number, height: number): Canvas;
  interface Canvas {
    getContext(contextType: "2d"): CanvasRenderingContext2D;
    toBuffer(type: "image/png"): Buffer;
  }
  interface CanvasRenderingContext2D {
    fillStyle: string;
    fillRect(x: number, y: number, width: number, height: number): void;
  }
}
