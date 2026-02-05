#include <deque>
#include <stdexcept>

class WorstCasePQA {
    std::deque<int> C, B, D_f, D_r;

    void pass(std::deque<int>& src, std::deque<int>& dst) {
        if (!src.empty()) {
            dst.push_back(src.front());
            src.pop_front();
        }
    }

    void bias() {
        if (!D_r.empty()) {
            if (!D_f.empty() && D_f.back() >= D_r.front()) {
                D_f.pop_back();
            } else {
                pass(D_r, D_f);
            }
        } else if (!D_f.empty() && (B.empty() || B.front() >= D_f.front())) {
            C.insert(C.end(), D_f.begin(), D_f.end());
            D_f.clear();
            B.clear();
        } else if (!B.empty()) {
            pass(B, C);
        }
    }

public:
    void insert(int x) {
        if (!C.empty() && C.front() >= x) {
            C.assign(1, x);
            B.clear();
            D_f.clear();
            D_r.clear();
        } else if (!C.empty() && C.back() >= x) {
            if (C.size() > 1) {
                B.assign(std::next(C.begin()), C.end());
            } else {
                B.clear();
            }
            int old_front = C.front();
            C.assign(1, old_front);
            D_f.assign(1, x);
            D_r.clear();
        } else {
            D_r.push_back(x);
        }
        bias();
        bias();
    }

    int delete_min() {
        bias();
        while (C.empty() && (!B.empty() || !D_f.empty() || !D_r.empty())) {
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
        return C.empty() && B.empty() && D_f.empty() && D_r.empty();
    }

    // Optional: Get the minimum without removing it
    int find_min() const {
        if (C.empty()) {
            throw std::out_of_range("Priority queue is empty");
        }
        return C.front();
    }
};