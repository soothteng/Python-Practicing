(define (vir-fib n)
  (if (< n 2)
      n
      (+ (vir-fib (- n 1))
         (vir-fib (- n 2)))))

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)


(define with-list
    (list
        (list 'a 'b) 'c 'd (list 'e)
    )
) 
(draw with-list)


(define with-quote
    '(
        (a b) c d (e)
    )
)
(draw with-quote)

(define helpful-list
    (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil
    ) nil)))
    )
)
(draw with-cons)

(define (list-concat a b)
    (if (null a)
        b
        (cons (car a) (list-concat (cdr a) b))
    )
)
(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)
(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)

(define (remove item lst)
    (filter (lambda (x) (not (= x item))) lst)
)
(expect (remove 2 '(1 2 3)) '(1 3))
