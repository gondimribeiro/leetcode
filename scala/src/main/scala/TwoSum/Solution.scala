/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they
 * add up to target. You may assume that each input would have exactly one solution, and you may not use
 * the same element twice. You can return the answer in any order.
 * https://leetcode.com/problems/two-sum/
 */
package twosum

object Solution extends App {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    val map = scala.collection.mutable.Map[Int, Int]()
    var count = 0

    for (num <- nums) {
      val comp = target - num

      map.get(comp) match {
        case None => map.put(num, count)
        case Some(index) => return Array(index, count)
      }

      count = count + 1
    }

    Array(0, 0)
  }

  println(twoSum(Array(2, 7, 11, 15), 9).toSeq.toString)
}
