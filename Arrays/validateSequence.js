// O(n) time | O(1) space - where n is the length of the array
function isValidSubsequence(array, sequence) {
    let arrIndex = 0
      let seqIndex = 0
      while (arrIndex < array.length && seqIndex < sequence.length) {
          if (array[arrIndex] === sequence[seqIndex]) seqIndex++;
          arrIndex++;
      }
      return seqIndex === sequence.length
  }