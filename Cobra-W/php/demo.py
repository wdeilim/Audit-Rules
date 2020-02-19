# -*- coding: utf-8 -*-

"""
    demo
    ~~~~

    just tamplates for rule

    :author:    LoRexxar <LoRexxar@gmail.com>
    :homepage:  https://github.com/LoRexxar/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 LoRexxar. All rights reserved
"""


class demo():
    """
    rule class
    
    ps: must temlates() for temlates.py
        just like CVI-1000() for CVI-1000.py
    """
    def __init__(self):

        self.svid = 1000
        self.language = "PHP"
        self.author = "LoRexxar"
        self.vulnerability = "Reflected XSS"
        self.description = "Reflected XSS"

        # status
        self.status = True

        # 部分配置
        self.match_mode = "function-param-regex"
        self.match = "echo|print|print_r|exit|die|printf|vprintf|trigger_error|user_error|odbc_result_all|ovrimos_result_all|ifx_htmltbl_result"
        self.vul_function = None

    def main(self, regex_string):
        """
        regex string input
        :regex_string: regex match string
        :return:
        """
        pass
