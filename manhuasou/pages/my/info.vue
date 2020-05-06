<template>
	<view>
		<view class="top_nav">
			<navigator url="../my/index" open-type="switchTab"><view class="back iconfont">&#xe606;</view></navigator>
		</view>
		<view class="info_list">
			<block v-for="(i, index) in menuList" :key="index">
				<view v-if="index === 0" class="info_item">
					<view class="info_left">{{ i.name }}</view>
					<view class="info_right">
						<view class="logining"><image :src="i.img"></image></view>
						<view class="iconfont">&#xe658;</view>
					</view>
				</view>
				<view v-if="index !== 0" class="info_item">
					<view class="info_left">{{ i.name }}</view>
					<view class="info_right">
						<view class="logining">{{ i.value }}</view>
						<view class="iconfont">&#xe658;</view>
					</view>
				</view>
			</block>
		</view>
	</view>
</template>

<script>
import '@/common/iconfont.css';
export default {
	data() {
		return {
			menuList: [
				{ name: '头像', img: '', url: '', iconfont: '\ue658', method: '', img: '../../static/images/douyin/4.jpg' },
				{ name: '用户名', img: '', url: '', iconfont: '\ue658', method: '', value: 'mmmaldalkdlladlaskdklas' },
				{ name: '昵称', img: '', url: '', iconfont: '\ue658', method: '', value: 'mmmaldalkdlladlaskdklas' },
				{ name: '性别', img: '', url: '', iconfont: '\ue658', method: '', value: '保密' },
				{ name: '星座', img: '', url: '', iconfont: '\ue658', method: '', value: '选择出生日期，系统自动转化为星座' },
				{ name: '领地', img: '', url: '', iconfont: '\ue658', method: '', value: '123' },
				{ name: '设置密码', img: '', url: '', iconfont: '\ue658', method: '', value: '123' },
				{ name: '绑定手机', img: '', url: '', iconfont: '\ue658', method: '', value: '150****2903' },
				{ name: '绑定邮箱', img: '', url: '', iconfont: '\ue658', method: '', value: '未绑定，可以在电脑端绑定邮箱' },
				{ name: '绑定QQ', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定' },
				{ name: '绑定微信', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定' },
				{ name: '绑定微博', img: '', url: '', iconfont: '\ue658', method: '', value: '去绑定' }
			],
			islogin: false
		};
	},
	methods: {},
	onLoad() {
		uni.getStorage({
			key: 'islogin',
			success: res => {
				this.islogin = res.data;
				if (this.islogin == null || this.islogin === false) {
					uni.redirectTo({
						url: '../user/login'
					});
				}
			}
		});
	}
};
</script>

<style lang="scss">
.top_nav {
	display: flex;
	width: 730rpx;
	padding-top: 20rpx;
	padding-left: 20rpx;
	align-items: center;
	background-color: #FF8C00;
	.iconfont {
		color: #ffffff;
		font-size: 45upx;
	}
}
.info_list {
	.info_item {
		background: #ffffff;
		padding: 20upx;
		width: 710upx;
		margin-top: 1upx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 70upx;
		.info_left {
			font-size: 30upx;
		}
		.info_right {
			display: flex;
			align-items: center;
			margin-top: -20upx;
			.logining {
				font-size: 30upx;
				border-radius: 20upx;
				padding-left: 40upx;
				padding-right: 20upx;
				margin-top: 20upx;
				image {
					border-radius: 100upx;
					width: 70upx;
					height: 70upx;
					margin-top: 10upx;
				}
			}
			.iconfont {
				font-size: 60upx;
				margin-top: 60upx;
			}
		}
	}
}
page {
	background: #c0c0c0;
}
</style>
