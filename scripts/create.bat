conan create . xiahan/stable -s build_type=Debug -o nvcloth:shared=True -o nvcloth:use_cuda=True -o nvcloth:use_dx11=False
conan create . xiahan/stable -s build_type=Debug -o nvcloth:shared=False -o nvcloth:use_cuda=True -o nvcloth:use_dx11=False
conan create . xiahan/stable -s build_type=Debug -o nvcloth:shared=True -o nvcloth:use_cuda=False -o nvcloth:use_dx11=True
conan create . xiahan/stable -s build_type=Debug -o nvcloth:shared=False -o nvcloth:use_cuda=False -o nvcloth:use_dx11=True
conan create . xiahan/stable -s build_type=Release -o nvcloth:shared=True -o nvcloth:use_cuda=True -o nvcloth:use_dx11=False
conan create . xiahan/stable -s build_type=Release -o nvcloth:shared=False -o nvcloth:use_cuda=True -o nvcloth:use_dx11=False
conan create . xiahan/stable -s build_type=Release -o nvcloth:shared=True -o nvcloth:use_cuda=False -o nvcloth:use_dx11=True
conan create . xiahan/stable -s build_type=Release -o nvcloth:shared=False -o nvcloth:use_cuda=False -o nvcloth:use_dx11=True