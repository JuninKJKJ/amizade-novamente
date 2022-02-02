#
#  Program to convert several questionnaries in YAML format to
#  Docx document.
#
#  Questionary Copyright (c) 2021 Carlos Pardo
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from _multichoice import Questionary
import random

project_material = {
   'yaml_files': [
      'es-material-properties.yaml',
      'es-material-wood.yaml',
      'es-material-stone.yaml',
      'es-material-metals.yaml',
      'es-material-plastics.yaml',
      ],
   'filename_output': 'es-material',
   'yaml_category': 'Materiales',
   'max_questions': 32,
   'random_seed': 1000,
}

project_machines = {
   'yaml_files': [
      'es-machines-simple.yaml',
      'es-machines-transmission1.yaml',
      'es-machines-transmission2.yaml',
      'es-machines-transmission3.yaml',
      'es-machines-transformation1.yaml',
      'es-machines-transformation2.yaml',
      ],
   'filename_output': 'es-machines',
   'yaml_category': 'Mecanismos',
   'max_questions': 32,
   'random_seed': 1000,
}

projects = [project_material, project_machines]
   
multichoice_path = ''
build_path = 'build'


def main():
   """Main program"""
   # Read yaml files
   for project in projects:
      questionary = Questionary()
      questions = []
      for yaml_file in project['yaml_files']:
         print(yaml_file)
         questionary.read_yaml(yaml_file, path=multichoice_path)
         questions = questions + questionary.questions

      # Write questions
      if project['random_seed']:
         random.seed(project['random_seed'])
      else:
         random.seed()
      random.shuffle(questions)
      if project['max_questions']:
         questions = questions[: project['max_questions']]
      questionary = Questionary()
      questionary.yaml_path = ''
      questionary.yaml_file = project['yaml_files'][0]
      questionary.filename = project['filename_output']
      questionary.header = {
         'Category': project['yaml_category'],
         'Title': 'Cuestionario global'
         }
      questionary.questions = questions
      questionary.docx_generate(path=build_path)
      print()


if __name__ == "__main__":
   main()
