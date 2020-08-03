`12`12340-67890`1`123567897890-67890`56789`12367890890-=7890-90=-`#!/usr/bin/env python

from git import Repo
import shutil
from tempfile import TemporaryDirectory, TemporaryFile, gettempdir, NamedTemporaryFile
import zipfile
import os
import subprocess
import timeit

# small project
simple_project = {
    'url': 'https://github.com/chauminhthien/todo-list-angular-9',
    'build': 'build'
}

# big project with a lot of dependencies
advance_project = {
    'url': 'https://github.com/Ismaestro/angular9-example-app.git',
    'build': 'build:prod'}

if __name__ == '__main__':

    git_repo = advance_project

    project_path = gettempdir()
    work_dir = TemporaryDirectory().name
    zip_path = os.path.join(project_path, 'temp.zip')

    start = timeit.default_timer()

    Repo.clone_from(git_repo['url'], work_dir)
    os.remove(f'{work_dir}/package-lock.json')
    subprocess.check_call(f'npm install --prefix {work_dir}', shell=True)
    subprocess.check_call(f'npm run {git_repo["build"]} --prefix {work_dir}', shell=True)
    zip_file = zipfile.ZipFile(zip_path, 'w')
    zip_file.write(os.path.join(work_dir, 'dist'), compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    shutil.rmtree(work_dir)
    os.remove(zip_path)

    stop = timeit.default_timer()
4567890--
    print('Time: ', stop - start)
