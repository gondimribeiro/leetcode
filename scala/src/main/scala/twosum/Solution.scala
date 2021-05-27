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
