import json
from pynvim import Nvim
import typing


from defx.base.column import Base
from defx.context import Context
from defx.view import View


class Column(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'indents'

        self.is_start_variable = True
        self.vars = {
            'last_space': '  ',
            'space': '| ',
            'last_file': '+ ',
            'file': '+ ',
        }
        opts = self.vim.call('defx_indents#get')

        for key in self.vars.keys():
            if key in opts:
                self.vars[key] = opts[key]

        self._indent = None

    def on_init(self, view: View, context: Context) -> None:
        self._context = context

    def get(self, context: Context, candidate: typing.Dict[str, typing.Any]) -> str:
        if candidate['is_root']:
            return ''

        # TODO キャッシュ使う
        #      candidateを元に実施するので辞書に入れていく必要あり

        indents = []
        path = candidate['action__path']
        level = candidate['level']
        for i in range(level+1):
            in_dir_name = sorted(path.parent.iterdir(), key=lambda x: (str(not x.is_dir()), x.name.lower()))
            last_name = None if len(in_dir_name) <= 0 else in_dir_name[-1].name
            is_last = last_name is not None and last_name == path.name

            if i == 0:
                if is_last:
                    indents.insert(0, self.vars['last_file'])
                else:
                    indents.insert(0, self.vars['file'])
            else:
                if is_last:
                    indents.insert(0, self.vars['last_space'])
                else:
                    indents.insert(0, self.vars['space'])
            path = path.parent

        self._indent = "".join(indents)
        return self._indent

    def length(self, context: Context) -> int:
        # TODO 2を変数から取る
        return 2 * int(max([x['level'] for x in context.targets]))
