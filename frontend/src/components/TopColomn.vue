<template>
  <div class="h-6">
    <el-menu class="el-menu-demo" style="border: 0;" mode="horizontal" background-color="#c45656" text-color="#ffffff"
             router="true"
             active-text-color="#ffd04b" @select="handleSelect">
      <el-menu-item index="/movies/index">电影列表</el-menu-item>
      <el-menu-item index="/home/userinfo">个人主页</el-menu-item>
      <el-sub-menu>
        <template #title>更多</template>
        <el-menu-item @click="changeUser">切换账号</el-menu-item>
        <el-menu-item index="/about">关于我们</el-menu-item>
        <el-menu-item @click="adminCheck">管理员入口</el-menu-item>
        <el-menu-item @click="returnWelcome">登出</el-menu-item>
      </el-sub-menu>
      <div class="flex-grow"/>
      <el-menu-item>{{ username }}</el-menu-item>
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import {ElMessage, ElMessageBox} from 'element-plus';
import {useRouter} from 'vue-router';
import {Action} from 'element-plus';
import axios from "axios"
import qs from "qs";
import {onBeforeMount, onMounted, ref} from "vue";

const route = useRouter()
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const returnWelcome = () => {
  ElMessageBox.confirm(
      '<strong>此操作会登出当前帐号，确定吗?</strong>',
      '系统提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        dangerouslyUseHTMLString: true
      }
  ).then(() => {
    axios.get('/user/signout').then(response => {
      if (response.data.errno == 0) {
        ElMessageBox.alert(
            '<strong style="font-size: 0.5cm">期待与您再次相遇</strong>',
            '登出成功',
            {
              dangerouslyUseHTMLString: true,
              confirmButtonText: '确定',
              draggable: true,
              type: 'info',
              callback: (action: Action) => {
                route.push('/')
              },
            }
        )
      }
    }).catch(response => {
      console.error(response.data.errno)
    });
  })
      .catch(() => {

      })
}

const changeUser = () => {
  ElMessageBox.confirm(
      '<strong>此操作会登出当前帐号，确定吗?</strong>',
      '系统提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        dangerouslyUseHTMLString: true
      }
  ).then(() => {
    axios.get('/user/signout').then(response => {
      if (response.data.errno == 0) {
        ElMessageBox.alert(
            '<strong style="font-size: 0.5cm">期待与您再次相遇</strong>',
            '登出成功',
            {
              dangerouslyUseHTMLString: true,
              confirmButtonText: '确定',
              draggable: true,
              type: 'info',
              callback: (action: Action) => {
                route.push('/login')
              },
            }
        )
      }
    }).catch(response => {
      console.error(response.data.errno)
    });
  }).catch(() => {

  })
}


onMounted(() => {
  setTimeout(() => askName(), 500)
})

let username = ref(null)

function askName() {
  axios
      .post("/user/askName/")
      .then((res) => {
        if (res.data.errno === 0) {
          username.value = res.data.username
        } else {
          username.value = '大傻逼'
        }
      }).catch((error) => {
    console.log(error)
  })
}


const adminCheck = () => {
  // 此处需要判断一下当前账号是否为管理员账号
  axios
      .post("/user/adminCheck/")
      .then((res) => {
        console.log(res)
        if (res.data.errno === 0) {
          ElMessage.success('欢迎您,管理员' + res.data.username)
          route.push('/admin/home')
        } else {
          route.push('/admin/error')
        }
      }).catch((error) => {
    console.log(error)
  })
}


</script>

<style>
.flex-grow {
  flex-grow: 0.94;
}
</style>

