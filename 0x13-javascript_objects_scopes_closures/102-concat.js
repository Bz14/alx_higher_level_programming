#!/usr/bin/node
const fs = require('fs');
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;
function concatFiles (sourceFile1, sourceFile2, destinationFile) {
  try {
    const data1 = fs.readFileSync(sourceFile1, 'utf8');
    const data2 = fs.readFileSync(sourceFile2, 'utf8');
    const concatenatedData = data1 + '\n' + data2 + '\n';
    fs.writeFileSync(destinationFile, concatenatedData);
  } catch (error) {
    console.error('Error concatenating files:', error);
  }
}

concatFiles(sourceFile1, sourceFile2, destinationFile);
