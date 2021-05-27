/**
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
package lengthlongestsubstring

object Solution {
  def lengthOfLongestSubstring(s: String): Int = {
    val map = scala.collection.mutable.Map[Char, Int] ()

    var maxStart, maxEnd = 0
    var currStart, currEnd = 0

    for (c <- s) {
      if (map.contains(c)) {
        if (maxEnd - maxStart < currEnd - currStart) {
          maxStart = currStart
          maxEnd = currEnd
        }

        currStart = map(c) + 1
        map.filterInPlace((c, pos) => pos >= currStart)
        map.update(c, currEnd)
      }
      else map.update(c, currEnd)

      currEnd += 1
    }

    if (maxEnd - maxStart < currEnd - currStart) {
      maxStart = currStart
      maxEnd = currEnd
    }

    maxEnd - maxStart
  }
}
