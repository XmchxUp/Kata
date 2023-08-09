#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  /*
  方法一：
    存储到数组中，遍历判断 O(n), O(n)
  */
  bool isPalindrome(ListNode *head) {
    std::vector<int> nums;
    while (head != nullptr) {
      nums.push_back(head->val);
      head = head->next;
    }
    for (int i = 0, j = nums.size() - 1; i < j; i++, j--) {
      if (nums[i] != nums[j]) {
        return false;
      }
    }
    return true;
  }

  /*
  方法二：
    快慢指针
      找到mid节点
      返回后半部分
      比较前面和后面
      可以恢复后面
      O(n) O(1)
  */
  ListNode *findMid(ListNode *head) {
    ListNode *fast = head, *slow = head;
    while (fast != nullptr && fast->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    return slow;
  }

  ListNode *reverse(ListNode *node) {
    if (node == nullptr || node->next == nullptr) {
      return node;
    }
    ListNode *head = reverse(node->next);
    node->next->next = node;
    node->next = nullptr;
    return head;
  }

  bool isPalindromeV2(ListNode *head) {
    if (head == nullptr) {
      return false;
    }
    // [5,3,5] mid=3 前部分[5,3] 后部分是[3,5]
    // [1,2,2,1] mid=2 前部分为[1,2] 后部分为[1,2]
    ListNode *mid = findMid(head);
    ListNode *p = head, *q = mid;
    q = reverse(q);
    while (q != nullptr) {
      if (p->val != q->val) {
        return false;
      }
      p = p->next;
      q = q->next;
    }
    return true;
  }
};
