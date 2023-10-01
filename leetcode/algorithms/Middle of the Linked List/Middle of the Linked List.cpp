struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
  ListNode *middleNode(ListNode *head) {
    auto p = head, q = head;

    while (p != nullptr && p->next != nullptr) {
      p = p->next->next;
      q = q->next;
    }
    return q;
  }
};