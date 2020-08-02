from git import Repo
import shutil
from tempfile import TemporaryDirectory, TemporaryFile, gettempdir, NamedTemporaryFile
import zipfile
import os
import subprocess
import timeit

# git_repo = 'https://github.com/Ismaestro/angular9-example-app.git'
git_repo = 'https://github.com/chauminhthien/todo-list-angular-9'

if __name__ == '__main__':

    # project_path = os.path.dirname(os.path.realpath(__file__))
    project_path = gettempdir()
    work_dir = os.path.join(project_path, 'temp')
    zip_path = os.path.join(project_path, 'temp.zip')

    start = timeit.default_timer()

    Repo.clone_from(git_repo, work_dir)
    os.remove(f'{work_dir}/package-lock.json')
    subprocess.check_call(f'npm install --prefix {work_dir}', shell=True)
    subprocess.check_call(f'npm run build --prefix {work_dir}', shell=True)
    zip_file = zipfile.ZipFile(zip_path, 'w')
    zip_file.write(work_dir, compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    shutil.rmtree(work_dir)
    shutil.rmtree(zip_path)

    stop = timeit.default_timer()

    print('Time: ', stop - start)
