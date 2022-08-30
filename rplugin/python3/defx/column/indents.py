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
        self.vars = {
            'indent1': '│ ',
            'indent2': '├ ',
            'indent3': '└ ',
            'indent4': '  ',
        }
        self.is_start_variable = True

    def on_init(self, view: View, context: Context) -> None:
        self._context = context

    def get(self, context: Context, candidate: typing.Dict[str, typing.Any]) -> str:
        if candidate['is_root']:
            return ''

        indents = []
        path = candidate['action__path']
        level = candidate['level']
        for i in range(level+1):
            in_dir_name = sorted(path.parent.iterdir(), key=lambda x: (str(not x.is_dir()), x.name.lower()))
            last_name = None if len(in_dir_name) <= 0 else in_dir_name[-1].name
            is_last = last_name is not None and last_name == path.name

            if i == 0:
                if is_last:
                    indents.insert(0, self.vars['indent3'])
                else:
                    indents.insert(0, self.vars['indent2'])
            else:
                if is_last:
                    indents.insert(0, self.vars['indent4'])
                else:
                    indents.insert(0, self.vars['indent1'])
            path = path.parent

        return "".join(indents)

    def length(self, context: Context) -> int:
        return 2 * int(max([x['level'] for x in context.targets]))

    def print(self, text: str) -> None:
        from os.path import expanduser
        with open(expanduser("~") + "/defx-indents.log", 'w') as f:
            f.write(text + "\n")
