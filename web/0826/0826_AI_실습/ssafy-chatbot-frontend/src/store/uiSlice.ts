import { createSlice } from '@reduxjs/toolkit';

interface UiState {
  isImagePreviewOpen: boolean;
  imagePreviewUrl: string | null;
}

const initialState: UiState = {
  isImagePreviewOpen: false,
  imagePreviewUrl: null,
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    showImagePreview(state, action) {
      state.isImagePreviewOpen = true;
      state.imagePreviewUrl = action.payload;
    },
    hideImagePreview(state) {
      state.isImagePreviewOpen = false;
      state.imagePreviewUrl = null;
    },
  },
});

export const { showImagePreview, hideImagePreview } = uiSlice.actions;
export default uiSlice.reducer;