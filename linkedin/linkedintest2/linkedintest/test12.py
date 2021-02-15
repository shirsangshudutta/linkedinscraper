from bs4 import BeautifulSoup
import json
import re
html="""
<div class="blended-srp-results-js pt0 pb4 ph0 container-with-shadow">
      <h3 class="search-results__total pt4 pb0 t-14 t-black--light t-normal pl5  clear-both">
          Showing 58,196 results
      </h3>

    <ul class="search-results__list list-style-none ">
          <li id="ember51" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember52" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="QBg/rzeQRGio0njIW4gGJQ==" data-control-name="search_srp_result" href="#" id="ember53" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember54" class="ivm-image-view-model ember-view">  <div id="ember55" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <img width="56" src="https://media-exp1.licdn.com/dms/image/C5603AQEkWRzw5uzx-g/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=48ra4AIUx3znyuxr6lwxR0q0Ne8msBxI2exnndc99JM" loading="lazy" height="56" alt="No alt text provided for this image" id="ember56" class="ivm-view-attr__img--centered EntityPhoto-circle-4  lazy-image ember-view">
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="QBg/rzeQRGio0njIW4gGJQ==" data-control-name="search_srp_result" href="#" id="ember57" class="search-result__result-link loading disabled ember-view">      <h3 id="ember58" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember59" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Student at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
      </p>

<!---->      </div>
<!---->  <div id="ember60" class="ember-view"><div id="ember61" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember63" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember64" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="VdjF9pdiRqOexioMBfjUkQ==" data-control-name="search_srp_result" href="/in/chandreyee-chowdhury-56244263/" id="ember65" class="search-result__result-link ember-view">      <figure class="search-result__image">
          <div id="ember66" class="ivm-image-view-model ember-view">  <div id="ember67" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <div id="ember129" class="presence-entity presence-entity--size-4 ember-view"><img title="Chandreyee Chowdhury" src="https://media-exp1.licdn.com/dms/image/C5603AQEr4kncUbK2HQ/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=6IEaT9_sFzAyZC-cIqaYo4VsNjnxjVnG8tGxLD0-q-U" loading="lazy" alt="Chandreyee Chowdhury" id="ember130" class="ivm-view-attr__img--centered EntityPhoto-circle-4  presence-entity__image EntityPhoto-circle-4 lazy-image ember-view">

<div id="ember131" class=" presence-entity__indicator presence-entity__indicator--size-4 presence-indicator hidden presence-indicator--size-4 ember-view">
<span class="visually-hidden">
    Status is offline
  </span></div></div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="VdjF9pdiRqOexioMBfjUkQ==" data-control-name="search_srp_result" href="/in/chandreyee-chowdhury-56244263/" id="ember69" class="search-result__result-link ember-view">      <h3 id="ember70" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="name-and-distance">
          <span class="name actor-name">Chandreyee Chowdhury</span>
        <span data-test-distance-badge="" id="ember71" class="distance-badge separator ember-view"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
      </span><!----></span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Associate Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Past: Research Fellow at Centre for Mobile Computing and Communication (CMCC), <strong>Jadavpur</strong> <strong>University</strong>
      </p>

<!---->      </div>
      <div class="search-result__actions">
        <div id="ember153" class="ember-view">    <button aria-label="Connect with Chandreyee Chowdhury. Associate Professor at Jadavpur University, Kolkata Area, India" class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary" data-control-name="srp_profile_actions" type="button" data-ember-action="" data-ember-action-154="154">
        Connect
    </button>
    <div id="ember155" class="ember-view"><div id="ember156" class="ember-view"><!----></div></div>
  
<!----></div>
      </div>
  <div id="ember72" class="ember-view"><div id="ember73" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember75" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember76" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="QyFDPFQaTEKUKudUKDi0LQ==" data-control-name="search_srp_result" href="/in/ram-sarkar-0ba8a758/" id="ember77" class="search-result__result-link ember-view">      <figure class="search-result__image">
          <div id="ember78" class="ivm-image-view-model ember-view">  <div id="ember79" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <div id="ember132" class="presence-entity presence-entity--size-4 ember-view"><img title="Ram Sarkar" src="https://media-exp1.licdn.com/dms/image/C5103AQG8SJHamhAAkg/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=ZpZl0Ojq4bIDtZtSYEyUfyFnEbwp5fA3upDzUoXSb7k" loading="lazy" alt="Ram Sarkar" id="ember133" class="ivm-view-attr__img--centered EntityPhoto-circle-4  presence-entity__image EntityPhoto-circle-4 lazy-image ember-view">

<div id="ember134" class=" presence-entity__indicator presence-entity__indicator--size-4 presence-indicator hidden presence-indicator--size-4 ember-view">
<span class="visually-hidden">
    Status is offline
  </span></div></div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="QyFDPFQaTEKUKudUKDi0LQ==" data-control-name="search_srp_result" href="/in/ram-sarkar-0ba8a758/" id="ember81" class="search-result__result-link ember-view">      <h3 id="ember82" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="name-and-distance">
          <span class="name actor-name">Ram Sarkar</span>
        <span data-test-distance-badge="" id="ember83" class="distance-badge separator ember-view"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
      </span><!----></span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Associate Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Past: Assistant Professor at <strong>Jadavpur</strong> <strong>University</strong>
      </p>

<!---->      </div>
      <div class="search-result__actions">
        <div id="ember157" class="ember-view">    <button aria-label="Connect with Ram Sarkar. Associate Professor at Jadavpur University, Kolkata Area, India" class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary" data-control-name="srp_profile_actions" type="button" data-ember-action="" data-ember-action-158="158">
        Connect
    </button>
    <div id="ember159" class="ember-view"><div id="ember160" class="ember-view"><!----></div></div>
  
<!----></div>
      </div>
  <div id="ember84" class="ember-view"><div id="ember85" class="ember-view"><!----></div>
</div>
</div>
</div>

</li>
<li id="ember87" class="search-results__list--cards mv5 ember-view">                <div class="mh5 mt3 mb4">
<!---->                <div class="display-flex align-items-baseline">
                  <h2 class="search-results__carousel-cluster-title t-20 t-black t-normal truncate mr3">
                    Job results for jadavpur university
                  </h2>
<!----><a data-control-name="search_srp_cluster_see_all" aria-label="See all: Job results for jadavpur university" href="/jobs/search/?keywords=jadavpur%20university" id="ember280" class="search-results__see-all-cards flex-shrink-zero link-without-hover-visited mlA ember-view">                        See all
</a>                </div>
              </div>
              <ul id="ember281" class="results-list display-flex pb3 ember-view">    <li data-test-search-result="JYMBII" id="ember283" class="search-result-card container ember-view"><a data-control-id="2iEWvNn7QRKmS4eP/lW+/w==" data-control-name="search_blended_srp_job_card" href="/jobs/view/1914247434/?refId=47c17607-4bbb-4942-a119-ca8b9e3650fd&amp;trk=d_flagship3_search_srp_top" id="ember284" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <img width="48" src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0?e=1600905600&amp;v=beta&amp;t=mNx8Ri2ySu4bJXh-Dy03m-GIxKaZ62t53QoMWYqHYdw" loading="lazy" height="48" alt="Jadavpur University" id="ember285" class="EntityPhoto-square-4 lazy-image ember-view">
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember286" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Office Assistant

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      Jadavpur University
    </p>

      <p class="subline-level-2-js t-12 t-black--light t-normal truncate">
        Kolkata, IN
      </p>

      <div class="search-result-card__social-proof-container mt1">
        <div id="ember287" class="flex-grow-0 search-result__social-proof ember-view">
<!---->
  <span class="search-result__social-proof-count t-12 t-black--light t-bold text-align-left">
      1 alum works here
  </span>
</div>
      </div>

      <p class="search-result-card__timestamp t-12 t-black--light t-normal truncate mtA">
        1 day ago
      </p>
</a><!---->  <div id="ember288" class="ember-view"><div id="ember289" class="ember-view"><!----></div>
</div>
</li>
    <li data-test-search-result="JYMBII" id="ember291" class="search-result-card container ember-view"><a data-control-id="OGzYR6I0TpuhxScoPj8IwQ==" data-control-name="search_blended_srp_job_card" href="/jobs/view/1820012203/?refId=47c17607-4bbb-4942-a119-ca8b9e3650fd&amp;trk=d_flagship3_search_srp_top" id="ember292" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <img width="48" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" height="48" alt="Assured job" id="ember293" class="EntityPhoto-square-4 lazy-image ghost-job ember-view">
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember294" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Java Developer (Freshers From IIT, NIT, Jadavpur University) For Kolkata

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      Assured job
    </p>

      <p class="subline-level-2-js t-12 t-black--light t-normal truncate">
        Kolkata, IN
      </p>

<!---->
      <p class="search-result-card__timestamp t-12 t-black--light t-normal truncate mtA">
        2 months ago
      </p>
</a><!---->  <div id="ember295" class="ember-view"><div id="ember296" class="ember-view"><!----></div>
</div>
</li>
    <li data-test-search-result="JYMBII" id="ember298" class="search-result-card container ember-view"><a data-control-id="Hgl3hgjSQeeWbVjTz2qmRg==" data-control-name="search_blended_srp_job_card" href="/jobs/view/1726084469/?refId=47c17607-4bbb-4942-a119-ca8b9e3650fd&amp;trk=d_flagship3_search_srp_top" id="ember299" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <img width="48" src="https://media-exp1.licdn.com/dms/image/C4E0BAQGDurOIUdK7nw/company-logo_100_100/0?e=1600905600&amp;v=beta&amp;t=lbMw_QGEm1Y1HK3DvyAzGJ-x1_D_6DsVinU0nuggZ-M" loading="lazy" height="48" alt="PwC India" id="ember300" class="EntityPhoto-square-4 lazy-image ember-view">
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember301" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Consultant - RDC TC MSOFT

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      PwC India
    </p>

      <p class="subline-level-2-js t-12 t-black--light t-normal truncate">
        Kolkata, IN
      </p>

      <div class="search-result-card__social-proof-container mt1">
        <div id="ember302" class="flex-grow-0 search-result__social-proof ember-view">
<!---->
  <span class="search-result__social-proof-count t-12 t-black--light t-bold text-align-left">
      10 alumni work here
  </span>
</div>
      </div>

      <p class="search-result-card__timestamp t-12 t-black--light t-normal truncate mtA">
        5 months ago
      </p>
</a><!---->  <div id="ember303" class="ember-view"><div id="ember304" class="ember-view"><!----></div>
</div>
</li>
</ul>

</li>          <li id="ember91" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember92" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="f0L+ac93Q+e6iYbYg+4aqg==" data-control-name="search_srp_result" href="#" id="ember93" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember94" class="ivm-image-view-model ember-view">  <div id="ember95" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"> <div class="EntityPhoto-circle-4-ghost-person ivm-view-attr__ghost-entity ">
<!---->  </div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="f0L+ac93Q+e6iYbYg+4aqg==" data-control-name="search_srp_result" href="#" id="ember96" class="search-result__result-link loading disabled ember-view">      <h3 id="ember97" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember98" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

<!---->
<!---->      </div>
<!---->  <div id="ember99" class="ember-view"><div id="ember100" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember102" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember305" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="MhKBZSluTT+43Aq6PAZMlQ==" data-control-name="search_srp_result" href="#" id="ember306" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember307" class="ivm-image-view-model ember-view">  <div id="ember308" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <img width="56" src="https://media-exp1.licdn.com/dms/image/C5103AQERohNOp7sFNw/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=B0XdxLBvsiq5YPnfTpdDaX0xqleKQ5BIEylTgGc77Pk" loading="lazy" height="56" alt="No alt text provided for this image" id="ember309" class="ivm-view-attr__img--centered EntityPhoto-circle-4  lazy-image ember-view">
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="MhKBZSluTT+43Aq6PAZMlQ==" data-control-name="search_srp_result" href="#" id="ember310" class="search-result__result-link loading disabled ember-view">      <h3 id="ember311" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember312" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Master's student.
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
      </p>

<!---->      </div>
<!---->  <div id="ember313" class="ember-view"><div id="ember314" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember104" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember315" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="sfNWryWsSkOld557tWbA1g==" data-control-name="search_srp_result" href="/in/riya-das-79836817a/" id="ember316" class="search-result__result-link ember-view">      <figure class="search-result__image">
          <div id="ember317" class="ivm-image-view-model ember-view">  <div id="ember318" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <div id="ember329" class="presence-entity presence-entity--size-4 ember-view"><img title="Riya Das" src="https://media-exp1.licdn.com/dms/image/C5103AQFY28N0r_B6Vw/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=BYJ0mcwDvu3mAlrEUCTvDXRUYPYuxwDeTwlOLCu4PiI" loading="lazy" alt="Riya Das" id="ember330" class="ivm-view-attr__img--centered EntityPhoto-circle-4  presence-entity__image EntityPhoto-circle-4 lazy-image ember-view">

<div id="ember331" class=" presence-entity__indicator presence-entity__indicator--size-4 presence-indicator hidden presence-indicator--size-4 ember-view">
<span class="visually-hidden">
    Status is offline
  </span></div></div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="sfNWryWsSkOld557tWbA1g==" data-control-name="search_srp_result" href="/in/riya-das-79836817a/" id="ember320" class="search-result__result-link ember-view">      <h3 id="ember321" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="name-and-distance">
          <span class="name actor-name">Riya Das</span>
        <span data-test-distance-badge="" id="ember322" class="distance-badge separator ember-view"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
      </span><!----></span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Student at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
      </p>

<!---->      </div>
      <div class="search-result__actions">
        <div id="ember323" class="ember-view">    <button aria-label="Connect with Riya Das. Student at Jadavpur University, Kolkata Area, India" class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary" data-control-name="srp_profile_actions" type="button" data-ember-action="" data-ember-action-324="324">
        Connect
    </button>
    <div id="ember325" class="ember-view"><div id="ember326" class="ember-view"><!----></div></div>
  
<!----></div>
      </div>
  <div id="ember327" class="ember-view"><div id="ember328" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember106" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember332" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="2EOm1dFDRGCDxXsThkvkLw==" data-control-name="search_srp_result" href="#" id="ember333" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember334" class="ivm-image-view-model ember-view">  <div id="ember335" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"> <div class="EntityPhoto-circle-4-ghost-person ivm-view-attr__ghost-entity ">
<!---->  </div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="2EOm1dFDRGCDxXsThkvkLw==" data-control-name="search_srp_result" href="#" id="ember336" class="search-result__result-link loading disabled ember-view">      <h3 id="ember337" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember338" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor (Economics) at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

<!---->
<!---->      </div>
<!---->  <div id="ember339" class="ember-view"><div id="ember340" class="ember-view"><!----></div>
</div>
</div>
</div>

</li>
<li id="ember108" class="search-results__list--cards mv5 ember-view">                <div class="mh5 mt3 mb4">
<!---->                <div class="display-flex align-items-baseline">
                  <h2 class="search-results__carousel-cluster-title t-20 t-black t-normal truncate mr3">
                    Groups about jadavpur university
                  </h2>
<!----><a data-control-name="search_srp_cluster_see_all" aria-label="See all: Groups about jadavpur university" href="/search/results/groups/?keywords=jadavpur%20university&amp;origin=CLUSTER_EXPANSION" id="ember341" class="search-results__see-all-cards flex-shrink-zero link-without-hover-visited mlA ember-view">                      See all
</a>                                  </div>
              </div>
              <ul id="ember342" class="results-list display-flex pb3 ember-view">    <li data-test-search-result="GROUP" id="ember344" class="search-result-card container ember-view"><a data-control-id="6LVF3/zJQ8WlyFmzdb9U7A==" data-control-name="search_blended_srp_group_card" href="/groups/62341/" id="ember345" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <div id="ember346" class="ivm-image-view-model ember-view">  <div id="ember347" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <img width="56" src="https://media-exp1.licdn.com/dms/image/C4E07AQFi2u-oV_fN5w/group-logo_image-shrink_400x400/0?e=1592899200&amp;v=beta&amp;t=iLI2SyJxsPXNXJoZxEcP7tw9gxhByinWjpsyaj1nweI" loading="lazy" height="56" alt="Jadavpur University" id="ember348" class="ivm-view-attr__img--centered EntityPhoto-square-4  lazy-image ember-view">
</div>
</div>
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember349" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Jadavpur University

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      Group • 1,432 members
    </p>

      <p class="subline-level-2-js mv2 t-12 t-black--light t-normal">
        <div id="ember350" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Jadavpur University Alumni Group  JU is a one of the most prestigious Indian University for modern day Engineering, Science and Arts studies.

<!----></div>
      </p>

<!---->
<!----></a><!---->  <div id="ember351" class="ember-view"><div id="ember352" class="ember-view"><!----></div>
</div>
</li>
    <li data-test-search-result="GROUP" id="ember354" class="search-result-card container ember-view"><a data-control-id="/ICMRMqJQV+v7S6v8Wzaqg==" data-control-name="search_blended_srp_group_card" href="/groups/698217/" id="ember355" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <div id="ember356" class="ivm-image-view-model ember-view">  <div id="ember357" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <img width="56" src="https://media-exp1.licdn.com/dms/image/C4D07AQFU3egx03g6Jw/group-logo_image-shrink_92x92/0?e=1592899200&amp;v=beta&amp;t=G3BYvaz3dwHbCKfRXNB5OCVk2kip76Mzlf-1ucd5y98" loading="lazy" height="56" alt="Jadavpur University MECHANICAL ENGINEERING Alumni" id="ember358" class="ivm-view-attr__img--centered EntityPhoto-square-4  lazy-image ember-view">
</div>
</div>
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember359" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Jadavpur University MECHANICAL ENGINEERING Alumni

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      Group • 949 members
    </p>

      <p class="subline-level-2-js mv2 t-12 t-black--light t-normal">
        <div id="ember360" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  All present and former Mechanical Engg students of Jadavpur University Kolkata are requested to join the group and help other alumni join as well.  This is the first such group of the Mech Dept and we need to create our identity as responsible builders of society.  Do invite your batchmates to join.

<!----></div>
      </p>

<!---->
<!----></a><!---->  <div id="ember361" class="ember-view"><div id="ember362" class="ember-view"><!----></div>
</div>
</li>
    <li data-test-search-result="GROUP" id="ember364" class="search-result-card container ember-view"><a data-control-id="xgW8x3zGQ/K3/FmpERF42Q==" data-control-name="search_blended_srp_group_card" href="/groups/72341/" id="ember365" class="search-result-card__link link-without-hover-visited display-flex flex-column flex-grow-1 pv4 ph2 ember-view">    <figure class="search-result-card__image display-flex justify-center mb2">
        <div id="ember366" class="ivm-image-view-model ember-view">  <div id="ember367" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <img width="56" src="https://media-exp1.licdn.com/dms/image/C5607AQElCkrKRvhwNA/group-logo_image-shrink_400x400/0?e=1592899200&amp;v=beta&amp;t=S1icuMt55188P52W2Z6qDA132babW0LF1MwrYmaHM1I" loading="lazy" height="56" alt="Jadavpur University Computer Science" id="ember368" class="ivm-view-attr__img--centered EntityPhoto-square-4  lazy-image ember-view">
</div>
</div>
    </figure>

    <h3 class="search-result-card__title search-result-card__truncated-text t-16 t-black t-bold">
        <div id="ember369" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  Jadavpur University Computer Science

<!----></div>
    </h3>

    <p class="subline-level-1-js mt1 t-14 t-black--light t-normal truncate">
      Group • 660 members
    </p>

      <p class="subline-level-2-js mv2 t-12 t-black--light t-normal">
        <div id="ember370" class="lt-line-clamp lt-line-clamp--multi-line ember-view" style="-webkit-line-clamp: 2">  This is a group for Jadavpur University Computer Science students and ex-students

<!----></div>
      </p>

<!---->
<!----></a><!---->  <div id="ember371" class="ember-view"><div id="ember372" class="ember-view"><!----></div>
</div>
</li>
</ul>

</li>          <li id="ember112" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember376" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="gsPzMqqcTiWOEH1iXyT3lg==" data-control-name="search_srp_result" href="#" id="ember377" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember378" class="ivm-image-view-model ember-view">  <div id="ember379" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"> <div class="EntityPhoto-circle-4-ghost-person ivm-view-attr__ghost-entity ">
<!---->  </div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="gsPzMqqcTiWOEH1iXyT3lg==" data-control-name="search_srp_result" href="#" id="ember380" class="search-result__result-link loading disabled ember-view">      <h3 id="ember381" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember382" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

<!---->
<!---->      </div>
<!---->  <div id="ember383" class="ember-view"><div id="ember384" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember114" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember385" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="uw+pFQBlRE6ZH7OO4BP1Uw==" data-control-name="search_srp_result" href="#" id="ember386" class="search-result__result-link loading disabled ember-view">      <figure class="search-result__image">
          <div id="ember387" class="ivm-image-view-model ember-view">  <div id="ember388" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"> <div class="EntityPhoto-circle-4-ghost-person ivm-view-attr__ghost-entity ">
<!---->  </div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="uw+pFQBlRE6ZH7OO4BP1Uw==" data-control-name="search_srp_result" href="#" id="ember389" class="search-result__result-link loading disabled ember-view">      <h3 id="ember390" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
      <span data-test-distance-badge="" id="ember391" class="distance-badge hidden separator ember-view"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

      <p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Current: Professor at Jadavpur University - ...(QIP), Nodal Cell (Pharmacy), <strong>Jadavpur</strong> <strong>University</strong>...
      </p>

<!---->      </div>
<!---->  <div id="ember392" class="ember-view"><div id="ember393" class="ember-view"><!----></div>
</div>
</div>
</div>

</li><li id="ember116" class="search-result search-result__occluded-item ember-view">        <div data-test-search-result="PROFILE" id="ember394" class="search-entity search-result search-result--person search-result--occlusion-enabled ember-view"><div class="search-result__wrapper">
  <div class="search-result__image-wrapper">
<a data-control-id="vbGUb01YTVeVhKMYBmlsnQ==" data-control-name="search_srp_result" href="/in/professor-somnath-mukherjee-63ab92a0/" id="ember395" class="search-result__result-link ember-view">      <figure class="search-result__image">
          <div id="ember396" class="ivm-image-view-model ember-view">  <div id="ember397" class="display-flex ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag ember-view"><!---->    <div id="ember408" class="presence-entity presence-entity--size-4 ember-view"><img title="Professor Somnath Mukherjee" src="https://media-exp1.licdn.com/dms/image/C4E03AQG6RHJu1dmeRA/profile-displayphoto-shrink_100_100/0?e=1598486400&amp;v=beta&amp;t=tt4KTFJExBJQi-zw2m4rwVBOcFEpxhFJAvmErV_Obqw" loading="lazy" alt="Professor Somnath Mukherjee" id="ember409" class="ivm-view-attr__img--centered EntityPhoto-circle-4  presence-entity__image EntityPhoto-circle-4 lazy-image ember-view">

<div id="ember410" class=" presence-entity__indicator presence-entity__indicator--size-4 presence-indicator hidden presence-indicator--size-4 ember-view">
<span class="visually-hidden">
    Status is offline
  </span></div></div>
</div>
</div>
      </figure>
</a>  </div>
  <div class="search-result__info pt3 pb4 ph0">
<a data-control-id="vbGUb01YTVeVhKMYBmlsnQ==" data-control-name="search_srp_result" href="/in/professor-somnath-mukherjee-63ab92a0/" id="ember399" class="search-result__result-link ember-view">      <h3 id="ember400" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="name-and-distance">
          <span class="name actor-name">Professor Somnath Mukherjee</span>
        <span data-test-distance-badge="" id="ember401" class="distance-badge separator ember-view"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
      </span><!----></span>


</h3>
</a>    <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor at Jadavpur University
    </p>

    <p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>

<!---->
<!---->      </div>
      <div class="search-result__actions">
        <div id="ember402" class="ember-view">    <button aria-label="Connect with Professor Somnath Mukherjee. Professor at Jadavpur University, Kolkata Area, India" class="search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary" data-control-name="srp_profile_actions" type="button" data-ember-action="" data-ember-action-403="403">
        Connect
    </button>
    <div id="ember404" class="ember-view"><div id="ember405" class="ember-view"><!----></div></div>
  
<!----></div>
      </div>
  <div id="ember406" class="ember-view"><div id="ember407" class="ember-view"><!----></div>
</div>
</div>
</div>

</li>
    </ul>
<div id="ember117" class="ember-view">          <div id="ember373" class="ember-view">  <div class="search-feedback-card__container--top-divider display-flex p5 t-sans t-14 justify-space-between">
      <div>
        <p class="t-16 t-black t-bold">
          Are these search results helpful?
        </p>
        <p class="t-14 t-black--light t-normal">
          Your feedback helps us improve.
        </p>
      </div>
      <div class="flex-shrink-zero">
        <button id="ember374" class="artdeco-button artdeco-button--circle artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="like-icon" class="artdeco-button__icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M17.51 11l-2.15-3a14.81 14.81 0 01-2.25-5.29L12.74 1H10.5A2.5 2.5 0 008 3.5v.58a9 9 0 00.32 2.39L9 9H4.66A2.61 2.61 0 002 11.4a2.48 2.48 0 00.39 1.43 2.48 2.48 0 00.69 3.39 2.46 2.46 0 001.45 2.92 2.47 2.47 0 000 .36A2.5 2.5 0 007 22h4.52a8 8 0 001.94-.24l3-.76H21V11h-3.49zM19 19h-2.12l-3.41.82A6 6 0 0112 20H7a.9.9 0 01-.9-.89v-.14l.15-1-1-.4a.9.9 0 01-.55-.83.93.93 0 010-.22l.3-.95-.73-.57a.9.9 0 01-.39-.74.88.88 0 01.12-.44l.46-.72-.46-.72a.88.88 0 01-.14-.51 1 1 0 011-.87h6.64l-1.3-4.7a9 9 0 01-.33-2.37v-.55a.5.5 0 01.5-.5h.95a17.82 17.82 0 002.52 6.22L16.6 13H19v6z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    
</span></button>
        <button id="ember375" class="ml3 artdeco-button artdeco-button--circle artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="dislike-icon" class="artdeco-button__icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 13V3h-4.5l-3-.76A8 8 0 0011.52 2H7a2.5 2.5 0 00-2.5 2.5 2.47 2.47 0 000 .36 2.46 2.46 0 00-1.42 2.92 2.48 2.48 0 00-.69 3.39A2.48 2.48 0 002 12.6 2.61 2.61 0 004.66 15H9l-.7 2.53a9 9 0 00-.3 2.39v.58a2.5 2.5 0 002.5 2.5h2.24l.37-1.67A14.81 14.81 0 0115.36 16l2.15-3H21zm-2-2h-2.4l-2.76 3.91a17.82 17.82 0 00-2.52 6.22h-.94a.5.5 0 01-.5-.5v-.56a9 9 0 01.33-2.37L11.5 13H4.92a1 1 0 01-1-.87.88.88 0 01.08-.51l.46-.72-.46-.72a.88.88 0 01-.12-.48.9.9 0 01.39-.7L5 8.43l-.19-.91a.93.93 0 010-.22.9.9 0 01.55-.83l1-.4L6.14 5v-.14A.9.9 0 017 4h5a6 6 0 011.46.18l3.42.82H19v6z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    
</span></button>
      </div>
  </div>
</div>

</div><div id="ember118" class="ember-view">          <div id="ember443" class="search-related-search__top--dividers ember-view"><div class="p5">
  <h2 class="t-16 t-black t-normal truncate inline">
    Try searching for
  </h2>
  <ul class="search-related-search__container">
      <li id="ember445" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20alumni&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember446" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>alumni</span></span>
</a></li>
      <li id="ember448" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20hr&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember449" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>hr</span></span>
</a></li>
      <li id="ember451" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20mba&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember452" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>mba</span></span>
</a></li>
      <li id="ember454" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20finance&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember455" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>finance</span></span>
</a></li>
      <li id="ember457" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20computer%20science&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember458" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>computer science</span></span>
</a></li>
      <li id="ember460" class="ember-view"><a data-control-name="related_searches" href="/search/results/all/?keywords=jadavpur%20university%20professor&amp;origin=RELATED_SEARCH_FROM_SRP" id="ember461" class="search-related-search__list-query ember-view">  <li-icon aria-hidden="true" type="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M21 19.67l-5.44-5.44a7 7 0 10-1.33 1.33L19.67 21zm-11-4.54A5.13 5.13 0 1115.13 10 5.13 5.13 0 0110 15.13z"></path>
</svg></li-icon>
  <span class="ml2">jadavpur university <span>professor</span></span>
</a></li>
  </ul>
</div></div>

</div>
<div id="ember119" class="ember-view">          <hr class="artdeco-divider mv0">
        <div id="ember411" class="pv5 artdeco-pagination ember-view">  <button disabled="" aria-label="Previous" id="ember412" class="artdeco-pagination__button artdeco-pagination__button--previous artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary artdeco-button--disabled ember-view">  <li-icon aria-hidden="true" type="chevron-left-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
  <path d="M7 8l4 5.9L9.5 15 5.3 8.8a1.22 1.22 0 010-1.6L9.5 1 11 2.1z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Previous
</span></button>

  <ul class="artdeco-pagination__pages artdeco-pagination__pages--number">
        <li data-test-pagination-page-btn="1" id="ember414" class="artdeco-pagination__indicator artdeco-pagination__indicator--number active selected ember-view">  <button aria-current="true" aria-label="Page 1">
    <span>1</span>
    <span class="a11y-text">Current page</span>
  </button>
</li>
        <li data-test-pagination-page-btn="2" id="ember416" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 2" data-ember-action="" data-ember-action-417="417">
    <span>2 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="3" id="ember419" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 3" data-ember-action="" data-ember-action-420="420">
    <span>3 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="4" id="ember422" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 4" data-ember-action="" data-ember-action-423="423">
    <span>4 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="5" id="ember425" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 5" data-ember-action="" data-ember-action-426="426">
    <span>5 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="6" id="ember428" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 6" data-ember-action="" data-ember-action-429="429">
    <span>6 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="7" id="ember431" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 7" data-ember-action="" data-ember-action-432="432">
    <span>7 </span>
  </button>
</li>
        <li data-test-pagination-page-btn="8" id="ember434" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 8" data-ember-action="" data-ember-action-435="435">
    <span>8 </span>
  </button>
</li>
        <li id="ember437" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view"><button aria-label="Page 9" data-ember-action="" data-ember-action-438="438">
  <span>…</span>
</button>
</li>
        <li data-test-pagination-page-btn="100" id="ember440" class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view">  <button aria-label="Page 100" data-ember-action="" data-ember-action-441="441">
    <span>100 </span>
  </button>
</li>
  </ul>

  <button aria-label="Next" id="ember442" class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="chevron-right-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
  <path d="M9 8L5 2.07 6.54 1l4.2 6.15a1.5 1.5 0 010 1.69L6.54 15 5 13.93z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Next
</span></button>
</div>

</div>
    <div id="ember120" class="pb5 ember-view"><section render-method="default" id="ember121" class="ad-banner-container ember-view"><iframe class="ad-banner" width="496" height="80" src="about:blank" scrolling="no" title="advertisement"></iframe>

<!----></section>
</div>
  </div>"""
#  t=BeautifulSoup(html,'html.parser').find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"})
html_source=BeautifulSoup(html,'html.parser')
# print(edusect)
for profile in html_source.find_all("div",{"class":"search-result__info pt3 pb4 ph0"}):
        if profile is not None:
            link1=profile.find("a",{"class":"search-result__result-link ember-view"})
            # print(link1)
            if link1 is not None:
             link='https://www.linkedin.com'+link1['href']
             print(link)
    # profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
