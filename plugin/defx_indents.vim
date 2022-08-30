scriptencoding utf-8
if exists('g:loaded_defx_indents')
  finish
endif
let g:loaded_defx_indents = 1

function! defx_indents#get() abort
  " TODO ユーザ設定の取り方を変える
  let indents = {}

  if exists('g:defx_indent_space')
    let indents['space'] = g:defx_indent_space
  endif

  if exists('g:defx_indent_last_space')
    let indents['last_space'] = g:defx_indent_last_space
  endif
  if exists('g:defx_indent_last_file')
    let indents['last_file'] = g:defx_indent_last_file
  endif
  if exists('g:defx_indent_file')
    let indents['file'] = g:defx_indent_file
  endif
  return indents
endfunction
