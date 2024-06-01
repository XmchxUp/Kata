#include <unordered_map>
#include <list>

class LRUCache {
 private:
  std::unordered_map<int, int> m_;
  std::list<int> l_;
  int capacity_;
  std::unordered_map<int, std::list<int>::iterator> pos_;

  void update(int key) {
    if (pos_.find(key) != pos_.end()) {
      l_.erase(pos_[key]);
    } else if (capacity_ == m_.size()) {
      int tkey = l_.back();
      m_.erase(tkey);
      l_.erase(pos_[tkey]);
      pos_.erase(tkey);
    }
    l_.push_front(key);
    pos_[key] = l_.begin();
  }

 public:
  LRUCache(int capacity) : capacity_(capacity) {}

  int get(int key) {
    if (m_.find(key) != m_.end()) {
      update(key);
      return m_[key];
    }
    return -1;
  }

  void put(int key, int value) {
    update(key);
    m_[key] = value;
  }
};
