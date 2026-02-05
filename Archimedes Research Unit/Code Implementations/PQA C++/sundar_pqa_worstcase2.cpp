#include <deque>
#include <stdexcept>

class WorstCasePQB {
    std::deque<int> C, D_f, D_r, DD;

    void passback(std::deque<int>& src, std::deque<int>& dst) {
        if (!src.empty()) {
            dst.push_front(src.back());
            src.pop_back();
        }
    }

    void pass(std::deque<int>& src, std::deque<int>& dst) {
        if (!src.empty()) {
            dst.push_back(src.front());
            src.pop_front();
        }
    }

    void bias() {
        if (!D_f.empty()) {
            if (!D_r.empty() && D_f.back() >= D_r.front()) {
                D_f.pop_back();
            } else {
                passback(D_f, D_r);
            }
        } else if (!D_r.empty()) {
            if (!DD.empty() && DD.front() < D_r.front()) {
                D_f.swap(DD);
                DD.clear();
                D_r.clear();
            } else {
                pass(D_r, C);
            }
        }
    }

public:
    void insert(int x) {
        if (!C.empty() && C.front() >= x) {
            C.assign(1, x);
            D_f.clear();
            D_r.clear();
            DD.clear();
        } else if (!C.empty() && C.back() >= x) {
            if (C.size() > 1) {
                D_r.assign(std::next(C.begin()), C.end());
            } else {
                D_r.clear();
            }
            int old_front = C.front();
            C.assign(1, old_front);
            D_f.clear();
            DD.assign(1, x);
        } else if (!DD.empty() && DD.front() >= x) {
            // Replace DD with x
            DD.assign(1, x);
        } else {
            // Add x to DD
            DD.push_back(x);
        }
        bias();
    }

    int delete_min() {
        bias();
        while (C.empty() && (!D_r.empty() || !D_f.empty() || !DD.empty())) {
            bias();
        }
        if (C.empty()) {
            throw std::out_of_range("Priority queue is empty");
        }
        int val = C.front();
        C.pop_front();
        return val;
    }

    bool empty() const {
        return C.empty() && D_f.empty() && D_r.empty() && DD.empty();
    }

    // Optional: Get the minimum without removing it
    int find_min() const {
        if (C.empty()) {
            throw std::out_of_range("Priority queue is empty");
        }
        return C.front();
    }

    // Optional: Get current size (approximate, may include dirty items)
    size_t size() const {
        return C.size() + D_f.size() + D_r.size() + DD.size();
    }
};