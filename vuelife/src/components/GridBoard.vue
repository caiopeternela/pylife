<template>
  <div>
    <div
      class="game-grid columns"
      @mousedown="isMouseDown = true"
      @mouseup="isMouseDown = false"
      @mouseleave="isMouseDown = false"
    >
      <div v-for="(col, indexX) in gridList" :key="indexX" class="game-column">
        <Cell
          v-for="(isAlive, indexY) in col"
          :key="indexY"
          :status-obj="isAlive"
          :x-pos="indexX"
          :y-pos="indexY"
          :is-mouse-down="isMouseDown"
          @wasUpdated="updateCellCount"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Cell from "@/components/CellBoard.vue";

export default {
  components: {
    Cell,
  },
  props: {
    message: {
      default: "",
      type: String,
    },
    currentSpeed: {
      default: 0,
      type: Number,
    }
  },
  data() {
    return {
      width: 46,
      height: 20,
      gridList: [],
      currentTick: 0,
      cellsAlive: 0,
      cellsCreated: 0,
      isMouseDown: false,
    };
  },
  computed: {},
  watch: {
    message: function (val) {
      if (val === "nextStep") {
        this.update();
        this.currentTick++;
      } else if (val === "redoSession") {
        this.reset();
      } else if (val === "randomSeed") {
        this.randomSeed();
      }
    },
  },
  created() {
    this.cellCalc();
  },
  methods: {
    cellCalc: function () {
      for (let i = 0; i < this.width; i++) {
        this.gridList[i] = [];
        for (let j = 0; j < this.height; j++) {
          this.gridList[i][j] = { isAlive: false };
        }
      }
      this.cellCount = this.width * this.height;
    },
    setCell: function (x, y, bool) {
      if (this.gridList[x][y].isAlive != bool) {
        this.gridList[x][y].isAlive = bool;
        this.updateCellCount(bool);
      }
    },
    update: function () {
      let newGrid = new Array(this.width * this.height);
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          let status = this.gridList[i][j].isAlive;
          let neighbours = this.getNeighbours(i, j);
          let result = false;
          switch (neighbours) {
            case 2:
              result = status;
              break;
            case 3:
              result = true;
              break;
          }
          newGrid[i * this.width + j] = result;
        }
      }
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          this.setCell(i, j, newGrid[i * this.width + j]);
        }
      }
    },
    getNeighbours: function (posX, posY) {
      let neighbours = 0;
      if (posX <= this.width && posY <= this.height) {
        for (let offsetX = -1; offsetX < 2; offsetX++) {
          for (let offsetY = -1; offsetY < 2; offsetY++) {
            let newX = posX + offsetX;
            let newY = posY + offsetY;
            if (
              (offsetX != 0 || offsetY != 0) &&
              newX >= 0 &&
              newX < this.width &&
              newY >= 0 &&
              newY < this.height &&
              this.gridList[posX + offsetX][posY + offsetY].isAlive == true
            ) {
              neighbours++;
            }
          }
        }
      }
      return neighbours;
    },
    reset: function () {
      this.currentTick = 0;
      this.cellsAlive = 0;
      this.cellsCreated = 0;
      this.gridList.forEach((col) => {
        col.forEach((cell) => {
          cell.isAlive = false;
        });
      });
    },
    updateCellCount: function (bool) {
      if (bool) {
        this.cellsAlive++;
        this.cellsCreated++;
      } else {
        this.cellsAlive--;
      }
    },
  },
};
</script>

<style scoped>

.game-grid {
  border-top: 1px solid #282a36;
  border-left: 1px solid #282a36;
  background-color: #6272a4;
  display: flex;
  flex: 1;
  justify-content: center;
}

.game-column {
  flex: 1;
  display: flex;
  justify-content: center;
  padding: 0;
  margin: 0 auto;
  flex-direction: column;
}

</style>