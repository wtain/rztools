
class RangeHelpers {
  public static range(start: number, end: number) {
      return Array(end - start + 1)
          .fill(0)
          .map((_, idx) => start + idx);
  }
}

export default RangeHelpers;