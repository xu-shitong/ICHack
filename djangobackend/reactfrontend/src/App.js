import logo from './logo.svg';
import './App.css';
import ReactAudioPlayer from 'react-audio-player';

function App(file) {
  return (
    <div className="App">
      <div class="px-4 py-3 my-5 text-center">
        <h1 class="display-5 fw-bold">Pitch perfect? Perfect pitch!</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">
            Upload your favourite tune. Upload your beautiful voice. Let the magic begin.
          </p>
        </div>
      </div>

      <div class="container">
        <div class="row mb-3">
          <div class="col-md-4">
            <div class="card mb-4 rounded-3 shadow-sm">
              <div class="card-header">
                <h3 class="my-0 fw-normal text-center">1. Favourite Tune 🎤</h3>
              </div>
              <div class="card-body">
                <div class="container">
                  <p>
                    Chug in your favourite tune. This is what the output will attempt to resemble!
                  </p>
                  <form method="POST" enctype="multipart/form-data" class="py-2">
                    <div class="row">
                      <div class="col-md-8">
                        <input type="file" accept=".wav" name="track" />
                      </div>
                      <div class="col-md-4">
                        <button type="submit"
                          class="w-100 btn btn-sm btn-outline-primary">Upload</button>
                      </div>
                    </div>
                  </form>
                  <p class="mt-2">
                    Test your upload.
                  </p>
                  <ReactAudioPlayer
                    src={{file}}
                    autoPlay
                    controls
                    class="py-2" style="width: 100%"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div >
  );
}

export default App;
