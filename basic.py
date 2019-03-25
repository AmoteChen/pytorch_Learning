import torch
from torch.autograd import Variable


#
# np_data = np.arange(6).reshape((2,3))
# torch_data = torch.from_numpy(np_data)
#
# tensor2array = torch_data.numpy()
# print(
#     '\nnumpy',np_data,
#     '\ntorch',torch_data,
#     "\ntensor2array",tensor2array
# )

# abs
# data = [-1,-2,1,2]
# tensor = torch.FloatTensor(data)
#
# print(
#     '\nabs'
#     '\nnumpy:' , np.mean(data),
#     '\ntorch' , torch.mean(tensor)
# )
#
# data = [[1,2],[3,4]]
# tensor = torch.FloatTensor(data)
#
# print(
#     '\nnumpy' , np.matmul(data,data), #data.dot(data)
#     '\ntorch' , torch.matmul(tensor,tensor)
# )

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor,requires_grad=True)
# print(tensor)
# print(variable)

# t_out = torch.mean(tensor*tensor)
# v_out = torch.mean(variable*variable)
#
# print(t_out,'\n',v_out)
#
# v_out.backward()
#v_out = 1/4*sum(var*var)
#d(v_out)/d(var)= 1/4*2*variable=variable/2
print(variable)
print(variable.data)
print(variable.data.numpy())