;;; .dir-locals.el
((typst-ts-mode . ((eval . (setq-local typst-ts-watch-options 
                                       (list "--root" 
                                             (expand-file-name
                                              (locate-dominating-file default-directory ".dir-locals.el"))
                                             "--open"))))))

