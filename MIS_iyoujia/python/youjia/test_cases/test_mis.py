#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/3/10 10:08
"""
"""
    重点：
    1、线上、预览线索CooperationID:13918 站点传selectsite（"3"）
    2、base文件修改mis地址，ownerH5_page修改H5地址

"""

from test_cases.page_obj import ownerH5_page,login_page,cooperation_page,contract_page,housemanagelist_page,leaguelist_page,nav_page,roomdetails_page,softoutfit_page,writeleague_page,roommanagelist_page
from models import myunit,mydef,configdb
from time import sleep
import unittest,os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR+r"\data\up.exe "+BASE_DIR+r"\images\2.jpg")

class TestData(myunit.MyTest):

    def test_createData(self):

        #获取顼亮给我传的参数，决定运行那个地址的自动化
        canshu = sys.argv[1]
        # canshu = "prod"

        # H5发布线索
        # H5 = ownerH5_page.OwnerH5(self.driver,canshu)
        # sleep(2)
        #
        # #打开H5招募网页
        # H5.openH5()
        # sleep(2)
        #
        # #点击成为业主
        # H5.Owner()
        # sleep(2)
        #
        # #输入业主姓名
        # H5.OwnerName()
        # sleep(2)
        #
        # #输入业主手机号
        # H5.OwnerPhone()
        # sleep(1)
        #
        # #输入图片验证码
        # H5.OwnerPicture()
        # sleep(2)
        #
        # #点击发送短信按钮
        # H5.OwnerMessage()
        # sleep(3)
        #
        # # 从数据库查询获取短信
        # msg = configdb.cord(17601052158)
        # sleep(2)
        #
        # #输入短信验证码
        # H5.OwnerMessageInput(msg)
        # sleep(2)
        #
        # #选择房源类型，随机选择的
        # H5.OwnerResidence()
        # sleep(2)
        #
        # #房源套数，随机输入，范围1-999
        # H5.OwnerRoomNum()
        # sleep(2)
        #
        # #选择省份
        # H5.Province()
        # sleep(2)
        #
        # #利用js，将省份下拉框滚动到最底部，让“新疆”可点击
        # H5.xiugai("province_select")
        # sleep(2)
        #
        # #点击选择新疆
        # H5.xinjiang()
        # sleep(1)
        #
        # #利用js，将市下拉框滚动到最底部，让“五家渠”可点击
        # H5.xiugai("city_select")
        # sleep(1)
        #
        # #点击选择五家渠
        # H5.wujiaqu()
        # sleep(1)
        #
        # #点击选择区
        # H5.qu()
        # sleep(1)
        #
        # #输入详情地址
        # H5.Address()
        # sleep(1)
        #
        # #提交
        # H5.SubmitBtn()
        # sleep(2)


        # MIS登录
        LL = login_page.LoginPage(self.driver,canshu)
        LL.Login()
        sleep(2)

        # #选择左侧基础服务
        NN = nav_page.NavPage(self.driver,canshu)
        NN.jichufuwu()
        sleep(2)

        #选择加盟管理
        NN.LeagueManage()

        #传参数线索ID
        #测试环境：①五家渠线索：737
        #          ②北京昌平线索：756
        #          ③上海线索：757
        #线上环境：线索ID：6321，13918
        CC = cooperation_page.CooperationPage(self.driver,canshu)
        CC.CooperationID(13918)
        sleep(2)

        #去掉五家渠，让五家渠数据可以显示
        CC.wujiaqu()
        sleep(2)

        #点击查询
        CC.Serch()
        sleep(2)

        #发起签约
        CC.StartLeague()
        sleep(2)

        #输入品牌使用费
        WW = writeleague_page.WriteLeague(self.driver,canshu)
        WW.LeagueMoney(100)
        sleep(1)

        #输入管理服务费
        WW.ServiceCharge(1)
        sleep(1)

        #输入有家分成比例
        WW.Proportions(1)
        sleep(2)

        #选择委托服务期限_开始时间
        WW.WTServicePeriodStart()
        sleep(2)

        #选择委托服务期限_结束时间
        WW.WTServicePeriodEnd()
        sleep(2)

        #时间插件没有收回去，如果没有收回去可能会遮住后面的定位，因此点击下提交按钮
        WW.Submit()
        sleep(2)

        #输入预期短租月收益
        WW.ExpectProfit()
        sleep(1)

        #输入长租月租金
        WW.LongMonthlyRent()
        sleep(2)

        #选择是加盟者本人房产
        WW.LeagueRoomYes()
        sleep(2)

        #选择房产证
        WW.DocumentTypePOC()
        sleep(2)

        # 点击上传图片
        WW.DocumentTypePhoto()
        sleep(3)

        #调用Auto上传图片
        os.system(BASE_DIR+r"/data/up.exe "+BASE_DIR+r"\images\2.jpg")
        sleep(5)

        # 选择房屋类型——民居
        WW.RoomType()
        sleep(2)
        WW.selectType()
        sleep(2)

        # 填写室、卫、厅、厨、阳台、建筑面积、楼层
        WW.RoomNum()
        sleep(1)
        WW.Parlor()
        sleep(1)
        WW.Toilet()
        sleep(1)
        WW.Kitchen()
        sleep(1)
        WW.Balcony()
        sleep(1)
        WW.Area()
        sleep(1)
        WW.fangzu()
        sleep(1)
        WW.Floor()
        sleep(1)

        #输入详细地址——街道地址、小区、楼
        WW.DetailedAddress()
        sleep(2)
        WW.Residentialquarters()
        sleep(2)
        WW.DoorNumbe()
        sleep(2)

        #地图扎点
        try:
            WW.maodian()
            sleep(2)
        except:
            print("地图扎点没扎上，尝试重新扎点")
            WW.maodian()
            sleep(2)

        #点击提交
        WW.Submit()
        sleep(1)

        #审核签约
        NN.LeagueApplyList()
        sleep(1)
        LLe= leaguelist_page.LeagueList(self.driver,canshu)
        LLe.Phone(18701016443)
        sleep(2)
        LLe.wujiaqu()
        sleep(3)
        LLe.Serach()
        sleep(2)

        #分配站点（重点！！！重点！！！重点！！！）
        po = leaguelist_page.LeagueList(self.driver,canshu)
        if po.LeagueState() == "待审核":
            sleep(2)

            #进入加盟详情页
            po.LeagueDetails()
            sleep(2)

            # 点击通过
            po.Pass()
            sleep(1)

            #点击下拉框
            po.SiteAlert()
            sleep(3)
            #分配站点（一定要注意数据的准确性）
            #测试环境：①北京昌平站：1
            #          ②五家渠站点：38
            #          ③上海站点：2
            #线上环境：五家渠站点（12）：3
            po.selectsite("7")
            sleep(2)

            #确认
            po.ConfirmBtn()
            sleep(1)
        else:
            print("状态不对")



        #编辑合同
        NN.LeagueApplyList()
        sleep(2)
        LLe.Phone(18701016443)
        sleep(2)
        LLe.wujiaqu()
        sleep(2)
        LLe.Serach()
        sleep(2)

        #进入合同详情页
        LLe.EidtContract()
        sleep(2)

        #点击编辑按钮
        CC = contract_page.Contract(self.driver,canshu)
        CC.Edit()
        sleep(2)

        #输入合同编号
        CC.ContractID()
        sleep(2)

        #点击上传图片按钮
        CC.ContractPhoto()
        sleep(4)

        #调用AutoIt完成上传图片
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #乙方姓名
        CC.FirstParty()
        sleep(2)

        #乙方身份证
        CC.IDcard()
        sleep(2)

        #选择权属（租赁）期限——开始时间
        CC.ServiceDataStart()
        sleep(1)

        #选择权属（租赁）期限——结束时间
        CC.ServiceDataEnd()
        sleep(2)

        #选择预计交房时间
        CC.RoomTime()
        sleep(2)
        CC.SelectDate()
        sleep(1)

        # 选择预计上线时间
        CC.OnlineDate()
        sleep(2)
        CC.SelectOnlineDate()
        sleep(2)

        #进入软装合同
        CC.SoftContract()
        sleep(1)

        #输入运营升级费用
        CC.OperationUpgradeFee(10)
        sleep(1)

        #输入软装费用
        CC.SoftPic()
        sleep(1)

        #床垫选择购买
        CC.BedBuy()
        sleep(1)

        #输入床垫费用
        CC.BedFee(10)
        sleep(1)

        #选择有家银行卡
        CC.Card()
        sleep(1)

        #输入品牌升级相关费用
        CC.UpgradeCost()
        sleep(1)

        #点击上传图片按钮并上传
        CC.SoftContractUp()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #点击提交审核
        CC.SubmissionOfAudit()
        sleep(2)
        CC.ConfirmBtn()
        sleep(2)

        #审核通过
        CC.Pass()
        sleep(2)
        CC.AlertPass()
        sleep(2)

        # 确认收款
        cc = contract_page.Contract(self.driver,canshu)
        cc.PassPayment()
        sleep(2)
        cc.PaymentAlert()
        sleep(2)
        cc.SoftContractPic()
        sleep(2)
        cc.SoftContractPicAlert()
        sleep(2)

        # 完成保洁
        NN.jichufuwu()
        sleep(1)
        NN.RoomManage()
        sleep(1)
        NN.HouseManage()
        sleep(1)

        HH = housemanagelist_page.HouseManagePage(self.driver,canshu)
        HH.wujiaqu()
        sleep(2)
        HH.FinishCleaning()
        sleep(2)
        HH.PassBtn()
        sleep(2)

        # 预约交接
        HH.Appointment()
        sleep(2)

        # 请录入与业主预约的交接时间——弹出时间插件
        HH.AppointmentDate()
        sleep(2)
        #点击此刻
        HH.ThisMoment()
        sleep(2)
        #填写备注信息
        HH.Remark()
        sleep(2)
        #确认按钮
        HH.Determine()
        sleep(2)

        # 点击完成交付
        HH.CompleteAppointment()
        sleep(2)

        #上传图片
        HH.AppointmentPicture()
        sleep(3)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(4)

        #预计筹建完成日——弹出时间控件
        HH.CompletionDate()
        sleep(2)
        #点击此刻
        HH.CompletionDateNow()
        sleep(2)

        #点击保存按钮
        HH.AppointmentSave()
        sleep(2)

        HH.wujiaqu()
        sleep(2)


        # 通知验收
        HH.NoticeCheck()
        sleep(2)
        HH.CheckDate()
        sleep(2)
        HH.ThisMoment()
        sleep(2)
        HH.NoticeCheckBtn()
        sleep(2)

        #点击完成验收
        HH.CompletionOfAcceptance()
        sleep(2)

        #点击保存
        HH.CompletionOfAcceptanceSave()
        sleep(2)

        # 弹窗点击编辑房屋，进入房屋详情页
        HH.AlertEditHouse()
        sleep(2)

        #编辑房屋
        HH.EditHouse()
        sleep(1)

        # 房屋标题
        title = "张佳恒测试" + mydef.rad_word(2)
        HH.HouseTitle(title)
        sleep(1)

        # 房屋简介
        Abbreviation = "这是一个测试房屋"
        HH.HouseNickAbbreviation(Abbreviation)
        sleep(1)

        # 淋浴数量
        HH.Shower(2)
        sleep(1)

        # 床的数量
        HH.SingleBed(2)
        sleep(1)

        # 上传封面照片
        HH.Cover()
        sleep(3)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #上传客厅照片
        HH.Parlour()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #上传卧室图片
        HH.Bedroom()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(4)

        #上传厨房图片
        HH.Kitchen()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #上传卫浴照片
        HH.Bathroom()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(5)

        #上传其他照片
        HH.Other()
        sleep(4)
        os.system(BASE_DIR + r"/data/up.exe " + BASE_DIR + r"\images\2.jpg")
        sleep(4)

        #点击提交
        HH.submitBtn()
        sleep(1)

        #获取房源ID
        HH.wujiaqu()
        sleep(1)
        id = HH.get_RoomID()
        sleep(1)

        #编辑房源
        NN.RoomManageList()
        sleep(1)

        #查询条件——输入房源id
        RR = roommanagelist_page.RoomManageListPage(self.driver,canshu)
        RR.SelectID(id)
        sleep(1)
        RR.wujiaqu()
        sleep(1)
        if RR.RoomState() == "待补充":

            #进入房源详情页
            RR.RoomId()
            sleep(1)

            #点击编辑按钮
            RR.Eidt()
            sleep(2)

            #输入房源简介
            RR.RoomIntroduce("测试测试测试")
            sleep(1)

            #输入日价
            RR.FloorPrice(80)
            sleep(1)

            #不设置周末价
            RR.NoSetUp()
            sleep(1)

            #输入押金
            RR.yajin(1)
            sleep(1)

            """
            默认都是选择1。
            1：不支持退款 2：宽松
            PS：Airbnb 1对应的是宽松
           """
            RR.SelectRefund("1")
            sleep(1)

            """SelectRefundChannel()选择渠道1：蚂蚁 2：有家 3：途家 4：Airbnb"""
            RR.SelectRefundChannel("2")
            sleep(1)
            RR.SelectRefund()
            sleep(1)
            RR.SelectRefundChannel("3")
            sleep(1)
            RR.SelectRefund()
            sleep(1)
            RR.SelectRefundChannel("4")
            sleep(1)
            RR.SelectRefund()
            sleep(1)

            #入住人数
            RR.pople(4)
            sleep(1)

            #输入其他须知
            RR.Other("测试ceshi测试ceshi")
            sleep(1)

            #点击提交
            RR.Submit()
            sleep(1)

        #进入房源并审核通过
        RR.SelectID(id)
        sleep(1)
        RR.wujiaqu()
        sleep(1)
        RR.RoomId()
        sleep(1)
        RR.Pass()
        sleep(1)
        RR.TwoPass()
        sleep(1)

        #判断房源状态是否改为上线
        RR.SelectID(id)
        sleep(1)
        RR.wujiaqu()
        sleep(1)
        assert RR.RoomState() == "已上线"



if __name__ == "__main__":
    unittest.main()
