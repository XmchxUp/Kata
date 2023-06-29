struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
  bool hasCycle(ListNode *head) {
    ListNode *fast = head, *slow = head;
    do {
      if (fast == nullptr || fast->next == nullptr) {
        return false;
      }
      fast = fast->next->next;
      slow = slow->next;
    } while (fast != slow);
    return true;
  }
};