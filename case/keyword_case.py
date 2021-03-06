import sys
sys.path.append('H:/PYwork/POMexample')
from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod

class KeyWordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(r"H:\PYwork\POMexample\config\keywords.xls")
        #拿到行数
        case_rows = handle_excel.get_lines()
        #循环行数，去执行每一条case
        if case_rows:
            for i in range(1,case_rows):
                is_run = handle_excel.get_col_value(i,3)
                #是否执行
                if is_run =='yes':
                    #拿到执行方法
                    method = handle_excel.get_col_value(i, 4)
                    #拿到操作值
                    send_value = handle_excel.get_col_value(i, 5)
                    #拿到操作元素
                    handle_method = handle_excel.get_col_value(i, 6)
                    #拿到预期结果 可能为‘’而不是None
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i,8)
                    #是否有输入数据
                    #if send_value:
                        #执行方法（输入数据，操作元素）
                    r_result = self.run_method(method,send_value,handle_method)
                    #没有输入数据
                        #执行方法（操作元素）
                    if except_result_method !='':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0]=='text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0]=='element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result :
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                    else:
                        print('预期结果为空')
                else:
                    print('no run')
        else:
            print('wrong')

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        if send_value=='' and handle_value!='':
            r_result = method_value(handle_value)
        elif send_value !='' and handle_value !='':
            r_result = method_value(send_value,handle_value)
        elif send_value != '' and handle_value =='':
            r_result = method_value(send_value)
        else:
            r_result = method_value()
        return r_result

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

if __name__ == '__main__':
    test = KeyWordCase()
    test.run_main()