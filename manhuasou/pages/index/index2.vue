<template>
	<view>
		<block v-if="navIndex == 0"><v-index></v-index></block>
		<block v-else-if="navIndex == 1"><v-index1></v-index1></block>
		<block v-else-if="navIndex == 2"><v-index2></v-index2></block>
		<block v-else-if="navIndex == 3"><v-index3></v-index3></block>
		<view class="nav_list">
			<view v-for="(item, i) in nav" :key="i" @click="setNavIndex(i)" :style="{ color: i == navIndex ? '#FF8C00' : 'black' }" class="nav_item">
				<view class="control">
					<view class="iconfont">{{ item.icon }}</view>
					<view style="margin-left: -2rpx;">{{ item.name }}</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
import index1 from '@/pages/index/index1.vue';
import index2 from '@/pages/list/index.vue';
import index3 from '@/pages/bookshelf/index.vue';
import index4 from '@/pages/my/index.vue';
import '@/common/iconfont.css';
export default {
	data() {
		return {
			nav: [
				{ name: '首页', icon: '\ue686', url: '/pages/index/index' },
				{ name: '分类', icon: '\ue659', url: '/pages/list/index' },
				{ name: '书架', icon: '\ue602', url: '/pages/bookshelf/index' },
				{ name: '我的', icon: '\ue64c', url: '/pages/my/index' }
			],
			navIndex: 0
		};
	},
	methods: {
		setNavIndex(i){
			this.navIndex=i
		}
	},
	components: {
		'v-index': index1,
		'v-index1': index2,
		'v-index2': index3,
		'v-index3': index4
	}
};
</script>

<style scoped lang="scss">
.nav_list {
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	bottom: 0;
	left: 0;
	width: 750rpx;
	background: #ffffff;
	height: 120rpx;
	font-size: 20rpx;
	.nav_item {
		width: 187.5rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 120rpx;
		.control {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
		}
	}
}


</style>
