# RedTeamGadget
## 简介
工具主要集合一些常见的RCE poc，方面在模拟攻击中使用这些poc，工具基于django的一个web应用。

## 使用
```shell
pip3 install requirements.txt
python3 manager.py runserver
```
## RCE检测清单
* confluence CVE-2022-26134
* hadoop 未授权访问
* jdwp debug RCE
* jenkins 未授权漏洞
* kibana<6.6.1未授权漏洞
* springboot actuator eureka未授权 RCE
* 未完待续

## 参考
* https://github.com/IOActive/jdwp-shellifier.git

## 免责声明
此工具仅用于日常测试，禁止恶意攻击使用。
