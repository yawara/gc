class OpenJtalk < Formula
  homepage "http://open-jtalk.sourceforge.net/"
  url "https://downloads.sourceforge.net/project/open-jtalk/Open%20JTalk/open_jtalk-1.08/open_jtalk-1.08.tar.gz"
  sha1 "34749abce5f8263ebbe9843b92407f4f0a742c66"

  resource "hts_engine API" do
    url "https://downloads.sourceforge.net/project/hts-engine/hts_engine%20API/hts_engine_API-1.09/hts_engine_API-1.09.tar.gz"
    sha1 "1c264c2bd29c87f49ace2c5d2b2fcd6b5b44b12c"
  end

  resource "voice" do
    url "http://downloads.sourceforge.net/project/open-jtalk/HTS%20voice/hts_voice_nitech_jp_atr503_m001-1.05/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz"
    sha1 "4298eaef57f86b7c502488aad2f95963da75f061"
  end

  resource "mei" do
    url "http://downloads.sourceforge.net/project/mmdagent/MMDAgent_Example/MMDAgent_Example-1.4/MMDAgent_Example-1.4.zip"
    sha1 "8e94593244c636bbe757eb848f1025a0111f4372"
  end

  def install
    resource("hts_engine API").stage do
      system "./configure", "--prefix=#{prefix}"
      system "make", "install"
    end

    args = %W[
      --with-hts-engine-header-path=#{include}
      --with-hts-engine-library-path=#{lib}
      --with-charset=UTF-8
      --prefix=#{prefix}
    ]

    system "./configure", *args

    inreplace "config.status", "-finput-charset=UTF-8 -fexec-charset=UTF-8", ""

    system "make", "install"

    resource("voice").stage do
      (prefix/"voice/m100").install Dir["*"]
    end

    resource("mei").stage do
      (prefix/"voice").install "Voice/mei"
    end
  end

  test do
    (testpath/"sample.txt").write "OpenJTalkのインストールが完了しました。"
    system bin/"open_jtalk",
      "-x", "#{prefix}/dic",
      "-m", "#{prefix}/voice/mei/mei_normal.htsvoice",
      "-ow", "out.wav",
      "sample.txt"
  end
end
