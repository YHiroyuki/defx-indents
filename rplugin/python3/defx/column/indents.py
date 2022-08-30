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
            'blank': '  ',
            'branch': '| ',
            'term': '+ ',
            'node': '+ ',
        }
        self._cache = {}
        self._length = max([len(var) for var in self.vars])

    def on_init(self, view: View, context: Context) -> None:
        self._cache = {}
        self._length = max([len(var) for var in self.vars])

    def on_redraw(self, view: View, context: Context) -> None:
        self._cache = {}

    def get(self, context: Context, candidate: typing.Dict[str, typing.Any]) -> str:
        if candidate['is_root']:
            return ''

        path = candidate['action__path']
        level = candidate['level']
        indents = []
        for i in range(level+1):
            absolute_path = str(path)

            if absolute_path not in self._cache:
                in_dir_names = sorted(path.parent.iterdir(), key=lambda x: (str(not x.is_dir()), x.name.lower()))
                last_name = None if len(in_dir_names) <= 0 else in_dir_names[-1].name
                self._cache[absolute_path] = last_name is not None and last_name == path.name

            is_last = self._cache[absolute_path]
            if i == 0:
                if is_last:
                    indents.insert(0, self.vars['term'])
                else:
                    indents.insert(0, self.vars['node'])
            else:
                if is_last:
                    indents.insert(0, self.vars['blank'])
                else:
                    indents.insert(0, self.vars['branch'])
            path = path.parent

        return "".join(indents)

    def length(self, context: Context) -> int:
        return self._length * int(max([x['level'] for x in context.targets]))
