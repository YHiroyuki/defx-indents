# Defx indents

Indentation extension for [defx.nvim](https://github.com/Shougo/defx.nvim)

## Usage

```vimL
:Defx -columns=icon:indents:filename:type
```
This column is used as a replacement for "indent".

## Configuration

```vimL
call defx#custom#column('indents', {
      \   'blank'    : '  ',
      \   'node'     : '├ ',
      \   'branch'   : '│ ',
      \   'term'     : '└ ',
      \ })
```
