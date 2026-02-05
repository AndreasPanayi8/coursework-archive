#include <deque>
#include <stdexcept>

class WorstCasePQA {
    std::deque<int> C, B, D_f, D_r;
    
    void _pass(std::deque<int>& A, std::deque<int>& B) {
        if (!A.empty()) {
            B.push_back(A.front());
            A.pop_front();
        }
    }
    
    void _bias() {
        if (!D_r.empty()) {
            if (!D_f.empty() && D_f.back() >= D_r.front()) {
                D_f.pop_back();
            } else {
                _pass(D_r, D_f);
            }
        } else if (!D_f.empty() && (B.empty() || B.front() >= D_f.front())) {
            C.insert(C.end(), D_f.begin(), D_f.end());
            D_f.clear();
            B.clear();
        } else if (!B.empty()) {
            _pass(B, C);
        }
    }
    
public:
    void insert(int x) {
        if (!C.empty() && C.front() >= x) {
            C = {x};
            B.clear();
            D_f.clear();
            D_r.clear();
        } else if (!C.empty() && C.back() >= x) {
            B.assign(C.begin() + 1, C.end());
            C = {C.front()};
            D_f = {x};
            D_r.clear();
        } else {
            D_r.push_back(x);
        }
        _bias();
        _bias();
    }
    
    int delete_min() {
        _bias();
        if (C.empty()) {
            throw std::out_of_range("Cannot delete from empty priority queue");
        }
        int val = C.front();
        C.pop_front();
        return val;
    }
};