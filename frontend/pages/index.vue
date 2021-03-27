<template>
  <div>
    <div class="toolbar" role="banner">
      <span style="margin-left: 5px">Errors Dashboard</span>
    </div>

    <div class="content" role="main">
      <div class="card-container">
        <div
          class="card card-small"
          v-for="(error, index) in ErrorNames"
          :key="index"
          @click="loadData(index)"
          :style="[selectedErrorIndex == index ? {'border':'thin solid #000000'} : {}]"
        >
          <span>{{ error }}</span>
        </div>
      </div>

      <vue-good-table
        @on-selected-rows-change="selectionChanged"
        :columns="columns"
        :rows="rows"
        :select-options="{ enabled: true }"
        :search-options="{
          enabled: true,
          placeholder: 'Search this table',
        }"
        style="width: 100%; height: 500px; padding: 25px"
      >
        <div slot="selected-row-actions">
          <button @click="actionOnClick()">{{ actionName }}</button>
        </div>
      </vue-good-table>

      <svg
        id="clouds"
        alt="Gray Clouds Background"
        xmlns="http://www.w3.org/2000/svg"
        width="2611.084"
        height="485.677"
        viewBox="0 0 2611.084 485.677"
      >
        <path
          id="Path_39"
          data-name="Path 39"
          d="M2379.709,863.793c10-93-77-171-168-149-52-114-225-105-264,15-75,3-140,59-152,133-30,2.83-66.725,9.829-93.5,26.25-26.771-16.421-63.5-23.42-93.5-26.25-12-74-77-130-152-133-39-120-212-129-264-15-54.084-13.075-106.753,9.173-138.488,48.9-31.734-39.726-84.4-61.974-138.487-48.9-52-114-225-105-264,15a162.027,162.027,0,0,0-103.147,43.044c-30.633-45.365-87.1-72.091-145.206-58.044-52-114-225-105-264,15-75,3-140,59-152,133-53,5-127,23-130,83-2,42,35,72,70,86,49,20,106,18,157,5a165.625,165.625,0,0,0,120,0c47,94,178,113,251,33,61.112,8.015,113.854-5.72,150.492-29.764a165.62,165.62,0,0,0,110.861-3.236c47,94,178,113,251,33,31.385,4.116,60.563,2.495,86.487-3.311,25.924,5.806,55.1,7.427,86.488,3.311,73,80,204,61,251-33a165.625,165.625,0,0,0,120,0c51,13,108,15,157-5a147.188,147.188,0,0,0,33.5-18.694,147.217,147.217,0,0,0,33.5,18.694c49,20,106,18,157,5a165.625,165.625,0,0,0,120,0c47,94,178,113,251,33C2446.709,1093.793,2554.709,922.793,2379.709,863.793Z"
          transform="translate(142.69 -634.312)"
          fill="#eee"
        />
      </svg>
    </div>
  </div>
</template>

<script>
// import the styles
import "vue-good-table/dist/vue-good-table.css";
import { VueGoodTable } from "vue-good-table";

export default {
  components: {
    VueGoodTable,
  },
  async asyncData({ $axios }) {
    try {
      const { resolved, unresolved, backlog } = await $axios.$get(
        "http://fast-api:8000/get_lists"
      );
      console.log(backlog)
      return {
        resolved,
        unresolved,
        backlog,
      };
    } catch (error) {
      console.log(
        `Couldn't get error lists:\n${error}\nDid you start the API?`
      );
      console.log(
        "HINT: You can comment out the full `asyncData` method and work with mocked data for UI/UX development, if you want to."
      );
    }
  },
  data() {
    return {
      selectedErrorIndex: -1,
      selectedRowsIndexes: [],
      resolved: [],
      unresolved: [],
      backlog: [],
      actionName: "",
      ErrorNames: ["Resolved", "Unresolved", "Backlog"],
      columns: [
        {
          label: "Text",
          field: "text",
        },
        {
          label: "Code",
          field: "code",
          type: "number",
        },
      ],
      rows: [],
      loadData: function (index) {
        /* 
        save the selected button index of the three buttons (resolved = 0, unresolved = 1, backlog = 2)
        and load the data upon this selection
        */
        this.selectedErrorIndex = index;
        if (index == 0) {
          this.rows = [...this.resolved];
          this.actionName = "unresolve";
        } else if (index == 1) {
          this.rows = [...this.unresolved];
          this.actionName = "resolve";
        } else {
          this.rows = [...this.backlog];
          this.actionName = "unresolve";
        }
      },
      actionOnClick: () => {
        /* 
        move the selected rows either from resolved to unresolved or vice versa
        or move the selected rows backlog to unresolved
        and refresh the table 
        */
        if (this.selectedErrorIndex == 0) {
          this.selectedRowsIndexes.forEach(selectedIndex => {
            this.unresolved.push(this.findErrorWithIndex(this.resolved, selectedIndex));
            this.resolved = [...this.filterErrorList(this.resolved, selectedIndex)]
          });
          this.rows = [...this.resolved];
    
        } else if (this.selectedErrorIndex == 1) {
          this.selectedRowsIndexes.forEach(selectedIndex => {
            this.resolved.push(this.findErrorWithIndex(this.unresolved, selectedIndex));
            this.unresolved = [...this.filterErrorList(this.unresolved, selectedIndex)]
          });
          this.rows = [...this.unresolved];

        }else {
          this.selectedRowsIndexes.forEach(selectedIndex => {
            this.unresolved.push(this.findErrorWithIndex(this.backlog, selectedIndex));
            this.backlog = [...this.filterErrorList(this.backlog, selectedIndex)]
          });
          this.rows = [...this.backlog];

        }
        this.selectedRowsIndexes = [];
      },
      findErrorWithIndex: (array, index) => {
        return array.find((element) => {
              return element.index === index;
            });
      },
      filterErrorList: (array, index) => {
        return array.filter((element) => {
              return element.index != index;
            });
      },
      selectionChanged: (params) => {
        // trace all the selcted elemetns and save the indexes
        this.selectedRowsIndexes = [];
        for (let selectedRow in params.selectedRows) {
          this.selectedRowsIndexes.push(params.selectedRows[selectedRow].index);
        }
        console.log(this.selectedRowsIndexes);
      },
    };
  },
};
</script>
