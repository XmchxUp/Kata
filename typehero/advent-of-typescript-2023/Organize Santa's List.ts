type SantasList<T extends readonly any[], V extends readonly any[]> = [
  ...T,
  ...V,
];
