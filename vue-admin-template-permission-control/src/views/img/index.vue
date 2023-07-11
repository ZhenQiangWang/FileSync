<template>
  <div>
<!--    <button @click="downloadImage">下载图像</button>-->
<!--    <img :src="imageData" alt="Base64 Image" style="width: 1000px;">-->
<!--    <img :src="imgUrl" alt="Base64 Image"/>-->
    <img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAFA3PEY8MlBGQUZaVVBfeMiCeG5uePWvuZHI////////////////////////////////////////////////////2wBDAVVaWnhpeOuCguv/////////////////////////////////////////////////////////////////////////wAARCACeASwDASIAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAIBAwT/xAAuEAACAgEDAwIFBAIDAAAAAAAAAQIRIRIxUQNBYXGRIjKBofATscHRQvFSYuH/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A9UpqLqjP1P8AqT1PnZ0jWlUBP6i4LOL3dHZbAG0txaDSbszSgNtWLQ0oUBilF8G2s+AopbCt/IC0E09hWQklsBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5tX1claUbSu+5oHPqRVWkWtg0mqZoESVtYQqSSSE5NPBmqVtJAFF71T8G6WY5TUVhWWspMCJal3ZbvBoAipYfcxKVVwdABD1JrfcOMm72+pYAhqTszS9NL2OgAipO8ip3viywBElLsxUuSwBFSpegqXOCwBMU8W+2SgAAAAAAAAAAAAAAAAAAAAxtJ1Y1LkxxTdjSgKJ1I1YM0rPkApxfconQigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxulZikm67+gFAnXHz7FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEzVxaRijTWCwBy/TdZXJ0V2727GgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGJp7NMS2/9OMMOLe1KvUDta5QvNHNJ4VrMnuvUyab1d/p4A6tpbsJp7M47QXb4n2rx/JfT+VrfyBdp9xa5Rz6cXGbVru3RW/Ua4QFWuRa5Oc4uUnwn/TNzLppLdoC009jSNTrZt3TRT2AWuULS3aOUW1pt/FSWwnevtTxbQHWxaOU81n/ABrG2f8ARS2e7t3hAWmnsxafdHOGE1gyCa0YeIgdRa5OUo7usIua47RYFXexpjdVu7NAAAAAAAAAAAAAAAAAAAAAAMbpN8ErqXKkmU1aohdPKvFcMA+ql2ZWrf0IfSbvPJUoW28NPFAHNJJ5yNaaeNjNF1q7Kt/Q1dOnLOGkgNUk3XcxdRNJ06NUWm3e7sldNqFYuq+1AU5ZarbyNWUuTHC32q7Ch8uFhUA1/A5VSNU7dVkz9NaHGlt7hQqVr2A1STk1wY+ok3jZ0NMlK8PxwHD5q7gUnaDaW4rO+K2EldeGBMZqSvO10F1E3VPcRg1xtRkYaZXgBLqpdmbLqKO6Zj6bfHuJdNvv2oC4y1K/NGkxi0kk6yUAAAAAAAAAAAAAAAAAAAAAAYLfDNM1J7NARqea3bpewlKsp47eTXCDXj1NajhN7Z3Ay/g3V+pqe7bwuTbWHaM+Gnx3yBRlv/ixab3QtXVqwIlOpeyEpPRjfwbKMHu6vyVFJRSWwEamo23eUsCMm5vOF4K0xUae3lmJQxVY4YFJpq1lC3wwqSSVcGgc5zqUe3K9xJy7b3gqSjvL3MUIxVdr5Anpzbi22trCbct/zBcVFYXYfA2nat53AiUn8WXh1+x0tXV5Jahm3u85KwneLAN+LMk2otpNG2quxakt8ARFycqb9zNbd1zX7FVC7VX6lOKYHPqSkm62r8/g6J3XZvszHpyn33NdXkDJPTFvgyDd6W7aV2VhprsZStvnAERnKTVNZukxKbUq2V/ai2o5ys+Q1G03umBM5NLCrF/sHNrpuW++xWiNJVVYVDSqaznyBibSau6XdkqUuXult6HSlnyNK48gRKb10tsq/YszSm9u1G0kBoAAmfyM5wUlVp75wdiFNN1tx5Alpq2+/wCfnqOpFt48f6K15qn37CU0m1wrAlReinbaZkYvRJ8+Do5JVsIy1evAEQtSynVvt5J01O3Ftenk6Rnq22sxdVYwBPUjc70t+n0/ouGFFJYrcS6ijKqD6lVjLvADqXppbsjpprDTxfbydNWGxGWpbUBCTTSl3Z0ryyI9XVTUXTo3WtVeaATXw7t0ZNNRpW8lOVVjtYjLUgMSvX7ERTVXe+Tq3SsiPUtq419QMlH4uLf52HUi3K/TtexT6lOqZspaa8ukBDVwSVv6GQS0yTTVruXKelK6z5CmnfgCOmqkvhpnVNtW1RMeopPjjyH1Elddm9wJ6ieptGdROlunnKyVPqaXVX+N/wAGvqJVfcCYtqMt7vjyarTfo3sVCWpXWCgOLjJNPl/0HalN7548L+TsAJVqll+SgAAAAAAAAAMeUSotO77/AMFgCXHN42oxxbb2yqLAESi5JW1gRhV3VPgsATGCXvaIj03FKnsv6OoAiXTUnffGQ4XX38lgCFB6avdGqNXX0KAHOPT00k8Jlac797+xQAhwzdr6oQg4xSvZ+5YAxq0TGDTWbr74LAHN9JOV4uuCnHC5VFACJQTqub+zCg6adW+6LAERhpk3eOPYz9PPjizoAIlDVfn7Ez6WrTn5WdQBEYaYtJ19CwAAAAAAAAAAAAAAD//Z">
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageData: "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAFA3PEY8MlBGQUZaVVBfeMiCeG5uePWvuZHI////////////////////////////////////////////////////2wBDAVVaWnhpeOuCguv/////////////////////////////////////////////////////////////////////////wAARCABSASwDASIAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAECAwT/xAAsEAACAgAFAgUEAgMAAAAAAAAAAQIRAxIhMUETUSJhcYGRQlLh8AShMrHx/8QAFgEBAQEAAAAAAAAAAAAAAAAAAAEC/8QAGBEBAQEBAQAAAAAAAAAAAAAAABEBIRL/2gAMAwEAAhEDEQA/APY3rRQAOLnO4046utV+TMsWam1apc0zp0o6ay08x0o3zvbA5yx5K0kmJY009K+Pyjo8GD4odGHKv1Ax1pZ8umyZOvKlVN5U/c6LCguL9R0Y1WtVQHJ48qjVW9w8edJrL8HXpRpLXTYnQhVagZjjScbaW+9cCeLOK433rf8As30YVWu97hYUEq1au9WBMKcpt5q2tUv+nUxCChdcmwOU8XI9m/Qw/wCQvpTbs6vDTdtbk6UdfDuZ6rn1p21po6JPHmr0So69GDdtFeHFpp8mkZlOfhay1J0YnjTjNx8Oi7fk6ywoyd2/ZkeDF3d6qgOTx50trrt5+p1wZucLluFhRVc0qNQioRpbAaAAAAAAAAAAEAAAFIBQQAUgAFAAHLqPtd8GnPwqmnLsaypcIUqqlQGFNt0/kNyb07G8qqqQpAIu4psPYJUqDVqmBjPL95K5Sp7WjWWPZfAaT3SYGZSaSa7WFJ27qjWVdkEktkgI5eG4tGcz5pb+xtpPdJjLH7V8AZUpWv8ARJTab27GssftXwXKuy+AMqTr3oz1Hy0jpSqtgklskgMxmmnqn6MKUmttTSVBJLZJAZuWTTypkUpK74N0qS7BxTAoAAAAAAAAAAAEAAFAhQAAAAAAAQn1r0M6p3q3fAG7FnGacnpW/wC9w/8AGnKvegO4MxqlT0omIrjvS5A2DiklFxb0fD0ChCOiT17gdgc8kYq0jLtp+Jvj90A6lOKjWrVebKopOk2kq9wOhTlkdW1bJbuuOdAOpTlTbVSe/YJuLd7Xx6AdQcfF339zatu3tQGhZxknm8SzbafJUtFSfarA7A5tOW0uCPVql71swOoOM81u/wCtCxTbdaNd9QOoMxu3deqRoAAAAAAAAAAAAAAAAAAQCghQABL8wKCFAAAACC13AoMuSW7oKSbpNCjQAAAjdEckt2KNAypRbpNWUCghQABAKCZl3Jnj9y+SUaBClAAAAAAAAAAAAAAMZXVaGwBNkUAAYyvyNgDMU1vRogABq1QAGcr8hONxaXKNkG9HLJJStU0bjGpN1uaBIqgAqMzVqkcunJPSnR2BNwZjFqV1wMrNFGZBnK/JmgCgTgoA4yw5Ntrkqi6VpaM6Az5Wo0/IlS7mwaRFaWpQAAAAAAAAAAAAAAAAABGAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf/Z"
    };
  },
  methods: {
    downloadImage() {
      const image = new Image();
      image.src = this.imageData;

      image.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;

        const ctx = canvas.getContext('2d');
        ctx.drawImage(image, 0, 0);

        canvas.toBlob((blob) => {
          const url = URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = url;
          link.download = 'image.png';
          link.click();
        }, 'image/png', 1); // 调整图像质量，范围为0-1
      }
    }
  }
};
</script>


