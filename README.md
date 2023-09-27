
# Defx indents

Indentation extension for [defx.nvim](https://github.com/Shougo/defx.nvim)
<img width="922" alt="image" src="https://user-images.githubusercontent.com/8401533/187561015-da94fad2-068b-4598-bb59-cd62ebb3b3fe.png">

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
↓ like this
<img width="914" alt="image" src="https://user-images.githubusercontent.com/8401533/187560842-21916e1d-e6ab-4b9a-aea9-43406f13c2fd.png">

