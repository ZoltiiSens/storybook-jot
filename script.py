import os


class StorybookCreator:
    def __init__(self, src_path, out_path, additional_path):
        self.menu = ''
        self.src_path = src_path
        self.out_path = out_path
        self.additional_path = additional_path

    def get_menu():
        return self.menu

    def formMenu(self, tab):
        self.menu = '<ul class="SB_side_menu">'
        self._formMenu('', tab + '\t')
        self.menu += '\n</ul>'
        return self.menu

    def create_fs(self, path):
        self.formMenu('\t\t\t')
        self._create_fs(path)

    def _create_fs(self, path):
        for elem in os.listdir(f'{self.src_path}/design/{path}'):
            if elem.endswith('.html'):
                self.formPage(f'{path}/{elem}')
            else:
                if not os.path.exists(f'{self.out_path}/design/{path}/{elem}'):
                    os.mkdir(f'{self.out_path}/design/{path}/{elem}')
                self._create_fs(f'{path}/{elem}')

    def formPage(self, path):
        content = ''
        with open(f'{self.src_path}/templates/page.html', 'r') as f:
            content = f.read()
        content = content.replace('///menu///', self.menu)
        content = content.replace('///path///', path.replace('.html','').replace('/', ' / ')[2:])
        content = content.replace('///title///', path.replace('.html','').split('/')[-1])
        content = content.replace('///file_path///', path)
        with open(f'{self.src_path}/design/{path}', 'r') as f:
            element = f.read()
            content = content.replace('///content///', element)
            content = content.replace('///code///', element.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
        with open(f'{self.out_path}/design{path}', 'w') as f:
            f.write(content)

    
    def _formMenu(self, path, tab):
        for elem in os.listdir(f'{self.src_path}/design/{path}'):
            if elem.endswith('.html'):
                self._addToMenu(tab, '<li>')
                self._addToMenu(tab, f'\t<a href="{self.additional_path}/{self.out_path}/design{path}/{elem}">{elem}</a>')
                self._addToMenu(tab, '</li>')
            else:
                self._addToMenu(tab, '<li>')
                tab += '\t'
                self._addToMenu(tab, '<ul class="hidden-ul inner-ul">')
                tab += '\t'
                self._addToMenu(tab, f'<p class="menu-title">{elem}</p>')
                self._formMenu(f'{path}/{elem}', tab)
                tab = tab[:-1]
                self._addToMenu(tab, '</ul>')
                tab = tab[:-1]
                self._addToMenu(tab, '</li>')

    def _addToMenu(self, tab, content):
        self.menu += f'\n{tab}{content}'



if __name__ == '__main__':
    storybookCreator = StorybookCreator(src_path='src', out_path='out', additional_path='/jot-storybook')
    storybookCreator.create_fs('')


# 123321




# result = []
# print(os.scandir('src/designs'))

# print(menu)
# print(menucreator.formMenu(''))
# menucreator.formPage('test.html')
# for path, folders, files in os.walk('designs'):
#     if len(files):
#         for file in files:
#             result.append(f'/{path}/{file}'.replace('\\', '/'))
    
# for elem in result:
#     print(elem)