#include <stack>
class MyQueue {
private:
  std::stack<int> s1{}, s2{};

public:
  MyQueue() {}

  void push(int x) { s1.push(x); }

  int pop() {
    int res{};
    if (!s2.empty()) {
      res = s2.top();
      s2.pop();
    } else {
      while (s1.size() > 1) {
        s2.push(s1.top());
        s1.pop();
      }
      res = s1.top();
      s1.pop();
    }

    return res;
  }

  int peek() {
    if (!s2.empty()) {
      return s2.top();
    }
    while (!s1.empty()) {
      s2.push(s1.top());
      s1.pop();
    }
    return s2.top();
  }

  bool empty() { return s1.empty() && s2.empty(); }
};
