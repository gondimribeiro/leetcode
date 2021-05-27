/**
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * https://leetcode.com/problems/add-two-numbers/
 */
package AddTwoNumbers

object Solution {
  class ListNode(_x: Int = 0, _next: ListNode = null) {
    var next: ListNode = _next
    var x: Int = _x
  }

  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {

    def loop(l1: ListNode, l2: ListNode, carryOne: Int): ListNode = {

      if (l1 == null && l2 == null && carryOne == 0)
        return null

      def getNext(l1: ListNode): (Int, ListNode) = {
        if (l1 == null) (0, null)
        else (l1.x, l1.next)
      }

      val (x1, next1) = getNext(l1)
      val (x2, next2) = getNext(l2)

      val sum = (x1 + x2 + carryOne)

      val x =  sum % 10
      val newCarry = sum / 10

      new ListNode(x, loop(next1, next2, newCarry))
    }

    loop(l1, l2, 0)
  }
}